"Create pydantic object for keeping track of statistics"

from typing import List

import numpy as np
from pydantic import BaseModel, Field


class Stats(BaseModel):
    """Object for tracking stats of optimization execution"""

    matrix: (np.ndarray)
    measurements: (np.ndarray)
    viol: List[float] = Field(default_factory=list)
    obj: List[float] = Field(default_factory=list)
    res: List[float] = Field(default_factory=list)

    def add_stat(self, x, x_p) -> None:
        """Update arrays storing performance statistics."""
        viol = float(np.linalg.norm(self.matrix @ x - self.measurements))
        if not self.viol:
            self.viol = [viol]
        else:
            self.viol.append(viol)

        obj = float(np.linalg.norm(x, ord=1))
        if not self.obj:
            self.obj = [obj]
        else:
            self.obj.append(obj)

        res = float(np.linalg.norm(x - x_p))
        if not self.res:
            self.res = [res]
        else:
            self.res.append(res)
