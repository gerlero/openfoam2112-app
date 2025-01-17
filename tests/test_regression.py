import pytest

import os
import subprocess
from pathlib import Path

from foamlib import AsyncFoamCase

@pytest.fixture
async def step():
    case = AsyncFoamCase(Path(os.environ["FOAM_TUTORIALS"]) / "incompressible" / "simpleFoam" / "backwardFacingStep2D")
    async with case.clone() as clone:
        yield clone

@pytest.mark.asyncio_cooperative
async def test_step(step):
    await step.run()
    assert "FOAM Warning" not in (step.path / "log.simpleFoam").read_text()

@pytest.mark.skipif(int(os.environ["FOAM_API"]) > 2312, reason="cfMesh removed from default installation")
def test_cf_mesh(): # https://github.com/gerlero/openfoam-app/issues/88
    subprocess.run(["cartesianMesh", "-help"], check=True)
