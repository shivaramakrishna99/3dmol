"""
Visualise structures using 3Dmol
"""

import subprocess
from pathlib import Path

from latch import large_task, workflow
from latch.resources.launch_plan import LaunchPlan
from latch.types import LatchAuthor, LatchFile, LatchMetadata, LatchParameter
from typing import Union, Optional
import py3Dmol

@large_task
def _3dmol_task(
    mol: Union[LatchFile, str],
    selectionName1: str = "name1",
) -> LatchFile:

    _3dmol_frame = f'''
     <script src="https://3Dmol.org/build/3Dmol-min.js" async></script>     
    <div style="height: 100%; width: 100%; position: relative;" class='viewer_3Dmoljs' data-pdb='1YCR' 
    data-select1='chain:A' data-style1='cartoon:color=spectrum' data-surface1='opacity:.7;color:white' data-select2='chain:B' data-style2='stick'></div>       
    
    '''
    view = 'view.html'
    with open(view, 'w') as f:
        f.write(_3dmol_frame)
    
    return LatchFile(view, f"latch:///3Dmol/{mol}.html")


"""The metadata included here will be injected into your interface."""
metadata = LatchMetadata(
    display_name="3Dmol",
    documentation="https://github.com/",
    author=LatchAuthor(
        name="Shivaramakrishna Srinivasan",
        email="shivaramakrishna.srinivasan@gmail.com",
        github="github.com/shivaramakrishna99",
    ),
    repository="https://github.com/shivaramakrishna99/",
    license="GPL-3.0",
    parameters= {
        "mol": LatchParameter(
            display_name="Molecule ",
            description="Enter PDB ID, upload a file, or provide a URL",
        ),
        "selectionName1": LatchParameter(
            display_name="First Selection",
            section_title="First Selection",
            description="Name your first selection"
        )
    },
    tags=[
        'Visualisation'
        ]
)


@workflow(metadata)
def _3dmol_wf(
    mol: Union[LatchFile, str],
    selectionName1: str = "name1",
) -> LatchFile:
    """3dmol DESCRIPTION
    LONG DESC
    """
    return _3dmol_task(
        mol=mol,
        selectionName1=selectionName1
        )


"""
Add test data with a LaunchPlan. Provide default values in a dictionary with
the parameter names as the keys. These default values will be available under
the 'Test Data' dropdown at console.latch.bio.
"""
# LaunchPlan(
#     _3dmol_wf,
#     "Test Data",
#     {
#         "read1": LatchFile("s3://latch-public/init/r1.fastq"),
#         "read2": LatchFile("s3://latch-public/init/r2.fastq"),
#     },
# )
