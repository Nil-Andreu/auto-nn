import numpy as np
from torch.utils.data import DataLoader
from auto_deep_learning.utils import DataCreator
from auto_deep_learning.utils.config import ConfigurationObject

# Set a random seed in numpy
np.random.seed(0)
conf_obj = ConfigurationObject()

class DatasetSampler():
    def __init__(
        self,
        data_creator: DataCreator,
    ):

        self.data_creator = data_creator
    
    def get_sampler(self):
        # TODO: For very small datasets, we might do not have valid

        return {
            data_creator_key: DataCreator(
                self.data_creator[data_creator_key],
                batch_size = conf_obj.batch_size[data_creator_key]
            ) for data_creator_key in self.data_creator.keys()
        }
