from .google_scanned_objects import *
from .realestate import *
from .deepvoxels import *
from .realestate import *
from .llff import *
from .llff_test import *
from .mvimgnet import *
from .ibrnet_collected import *
from .realestate import *
from .spaces_dataset import *
from .nerf_synthetic import *
from .llff_render import *
from .nerf_synthetic_render import *
from .nmr_dataset import *

dataset_dict = {
    "spaces": SpacesFreeDataset,
    "google_scanned": GoogleScannedDataset,
    "realestate": RealEstateDataset,
    "deepvoxels": DeepVoxelsDataset,
    "nerf_synthetic": NerfSyntheticDataset,
    "llff": LLFFDataset,
    "ibrnet_collected": IBRNetCollectedDataset,
    "llff_test": LLFFTestDataset,
    "mvimgnet": MVTestDataset,
    "llff_render": LLFFRenderDataset,
    "nerf_synthetic_render": NerfSyntheticRenderDataset,
    "nmr": NMRDataset,
}
