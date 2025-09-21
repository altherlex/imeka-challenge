Code assessment workflow - Q2

We would like to understand your workflow and thought process when assessing new code,
especially in a language you haven’t used.
Imeka has developed the trk-io project as an open-source library to help working with the
TrackVis file format. This specific data structure in the trk-io repository contains a data structure
that is used to store streamlines information, which represent tracts of the white matter that are
reconstructed from diffusion MRI.

1. Please summarize your thought process and workflow to understand the data structure,
to answer the questions below and how you found the information when you were not
familiar with some concepts.

2. From lines 8-12, what’s the purpose of the “derive” line? What could be a reason to
create an “ArraySequence” structure in a project like “trk-io”?

-----

1. Workflow: 
* Check for documentation (README, code commenst, unit tests, examples, mopcked data, etc)
* Understand the app structure
* Inspect structure definitions
* Compare syntax with other languages
* Try to understand the domain language of the health area

2. “derive” line:
It's a interface to import functions Debug, Clone, PartialEq.
Without derive, we’d have to implement them manually.

ArraySequence efficiently stores and handles variable-length 3D streamlines; ideal to handle large diffusion MRI datasets.