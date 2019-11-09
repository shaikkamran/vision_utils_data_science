from typing import Union, List
from dataclasses import dataclass

import numpy as np
import pandas as pd

@dataclass
class ImgData:
    imgs: Union[List[str], np.array] = None
    labels: Union[List[str], np.array] = None
    
    