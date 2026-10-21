# Release checklist

- [x] Prepare publication copies limited to Doublets 2 and 4.
- [x] Preserve originals and clear source notebook outputs/execution counts.
- [x] Copy and checksum required local data and manuscript references.
- [x] Execute preprocessing, receptor annotation, SHM analysis, and manuscript figure sections.
- [x] Provide a tested command for checkpoint-based manuscript figure rendering.
- [x] Diagnose both clustering discrepancies and resolve Sp55's AnnData materialization issue.
- [x] Restore the author-approved historical 30% ERCC cutoff for Doublets 2 in the release code and Methods; retain 20% for Doublets 4.
- [x] Verify the IL10/cytotoxic Discussion statement against the Sp55 overlap check: 53 of 57 IL10-positive interactions also meet the existing positivity criterion for at least one cytotoxic marker. The earlier Doublets 2 union flag is not an unresolved Methods requirement.
- [x] Author requested upload of the code on 20 October 2026.
- [x] Build and verify the 7,829-file auxiliary data archive.
- [x] Install the release Python dependencies in a clean environment and rerun all five figure sections.
- [x] Resolve the non-spheromer Sp46 partition difference with an explicit subset copy before PCA; verify all five fresh partitions and named labels against the manuscript objects.
- [ ] Add and verify the other paper workflows before claiming complete paper reproduction.
- [ ] Select a license and final citation/archive identifiers.
- [ ] Publish the large data archive at a persistent download location and add its URL.
- [ ] Finalize the repository's public release and data availability statement.
