"""Compare generated PDFs to saved exports; requires requirements-qa.txt.

Reports differences without treating successful execution as figure identity.
"""
from pathlib import Path
import json,re,hashlib
import numpy as np
from PIL import Image
import pypdfium2 as pdfium
from pypdf import PdfReader
repo=Path(__file__).resolve().parents[1];audit=repo/'results/figure_comparison';out=audit/'plot_comparisons';out.mkdir(parents=True,exist_ok=True)
cache={}
def raster(p):
 if str(p) in cache:return cache[str(p)]
 doc=pdfium.PdfDocument(str(p));page=doc[0];im=page.render(scale=1.5).to_pil().convert('RGB');page.close();doc.close();cache[str(p)]=im;return im

def metric(a,b):
 x=raster(a);y=raster(b)
 if x.size!=y.size:return {'same_size':False,'generated_size':x.size,'reference_size':y.size,'pixel_exact':False}
 ar=np.asarray(x).astype(float);br=np.asarray(y).astype(float)
 return {'same_size':True,'pixel_exact':bool(np.array_equal(ar,br)),'mean_absolute_pixel_difference':round(float(abs(ar-br).mean()),6),'changed_pixel_fraction':round(float(np.any(abs(ar-br)>5,axis=2).mean()),6)}
refs={}
for p in (repo/'data/manuscript_plot_references').glob('*/*.pdf'):refs.setdefault(p.name,[]).append(p)
results=[]
for p in sorted((repo/'results').glob('*/*.pdf')):
 if p.name not in refs:
  results.append({'generated':str(p.relative_to(repo)),'status':'no_matching_reference_filename'});continue
 candidates=refs[p.name];candidates.sort(key=lambda p:max(re.findall(r'\d{8}',p.parent.name) or ['00000000']),reverse=True)
 latest=candidates[0];m=metric(p,latest)
 exact=[]
 for c in candidates:
  if metric(p,c).get('pixel_exact'):exact.append(str(c.relative_to(repo)))
 row={'generated':str(p.relative_to(repo)),'latest_reference':str(latest.relative_to(repo)),**m,'exact_matching_references':exact}
 results.append(row)
 # Visual comparison panel for representative final figures and mismatches.
 if p.name.startswith(('umap_','dotplot_','barplot_','violinplot_','heatmap_')):
  a=raster(p);b=raster(latest)
  maxw=900
  imgs=[]
  for im in [b,a]:
   if im.width>maxw:im=im.resize((maxw,round(im.height*maxw/im.width)))
   imgs.append(im)
  w=sum(im.width for im in imgs)+30;h=max(im.height for im in imgs)+40
  panel=Image.new('RGB',(w,h),'white');from PIL import ImageDraw
  draw=ImageDraw.Draw(panel);draw.text((5,5),'Saved manuscript export',fill='black');draw.text((imgs[0].width+25,5),'Regenerated',fill='black')
  panel.paste(imgs[0],(0,30));panel.paste(imgs[1],(imgs[0].width+30,30));panel.save(out/(p.parent.name+'__'+p.stem+'.png'))
(audit/'plot_comparison.json').write_text(json.dumps(results,indent=2))
print('Plots',len(results),'matching reference filenames',sum('latest_reference' in r for r in results),'pixel identical latest',sum(r.get('pixel_exact',False) for r in results),'exact match to any recorded version',sum(bool(r.get('exact_matching_references')) for r in results))
for r in results:
 if 'latest_reference' in r:print(Path(r['generated']).name, 'EXACT' if r['pixel_exact'] else 'DIFF',r.get('mean_absolute_pixel_difference', 'dimensions differ'))
