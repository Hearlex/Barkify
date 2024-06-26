import functools
from torch.utils.data import DataLoader

from .data import Dataset
from .data import Text2semanticCollateFn, Semantic2coarseCollateFn
stage_collate = [Text2semanticCollateFn, Semantic2coarseCollateFn]

from .tokenizer import HunPhonemeTokenizer

def StageDataloader(params, stage=1, file='train') -> DataLoader:
    tokenizer = HunPhonemeTokenizer() # TODO: add more tokenizer - Egészen pontosan hungarian tokenizer
    dataset = Dataset(file=file, tokenizer=tokenizer, **params.dataset)
    collate_fn = functools.partial(stage_collate[int(stage) - 1], **params.collate_fn)

    loader = DataLoader(dataset, collate_fn=collate_fn, **params.dataloader) 
    return loader