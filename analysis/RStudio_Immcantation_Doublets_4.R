# Doublets 4: SHazaM mutation summaries from Change-O/AIRR annotations.
# Run from analysis/ after supplying the input table. Execution evidence is summarized in ../VALIDATION_REPORT.md.
# Required R packages: airr, shazam, dplyr.
library(shazam)
library(dplyr)

db <- airr::read_rearrangement("../data/Doublets/data/smartseq_doublets_4_analysis/changeo/changeo_IGH_IGKL/allcells_outfmt_immcantation_db-pass_parse-select_clone-pass_germ-pass.tsv")

#subset on heavy chain
db <- subset(db, locus == "IGH")
#extract sortedpop and barcode from sequence id
db <- db %>%
  mutate(sortedpop = sapply(strsplit(sequence_id, "_|;|="), function(parts) parts[3]))

db <- db %>%
  mutate(barcode = sapply(strsplit(sequence_id, "_|;"), function(parts) paste(parts[8], parts[9], sep = "-")))

# Calculate aggregate CDR/FWR mutation frequencies used by the manuscript plots.
db_obs <- observedMutations(db, sequenceColumn="sequence_alignment",
                            germlineColumn="germline_alignment_d_mask",
                            frequency=TRUE,
                            regionDefinition = IMGT_V,
                            nproc=1)



# Calculate individual VDJ-region summaries separately.
db_obs_regions <- observedMutations(db, sequenceColumn="sequence_alignment",
                                   germlineColumn="germline_alignment_d_mask",
                                   frequency=TRUE,
                                   regionDefinition=IMGT_VDJ_BY_REGIONS,
                                   nproc=1)

# Export annotated heavy-chain tables.
write.table(db_obs, "../data/Doublets/data/smartseq_doublets_4_analysis/changeo/changeo_IGH_IGKL/allcells_outfmt_immcantation_db-pass_parse-select_clone-pass_germ-pass_Formatted_withSHM.tsv", sep = "\t", row.names = FALSE, quote = FALSE)

write.table(db_obs_regions, "../data/Doublets/data/smartseq_doublets_4_analysis/changeo/changeo_IGH_IGKL/allcells_outfmt_immcantation_db-pass_parse-select_clone-pass_germ-pass_Formatted_withSHM_VDJRegions.tsv", sep = "\t", row.names = FALSE, quote = FALSE)

