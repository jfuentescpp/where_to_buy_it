/***********************************
 * Exact Street2Shop Dataset, 2015 *
 ***********************************/

This dataset contains exact street2shop pairs and the retrieval sets for 11 clothing categories:
    - bags
    - belts
    - dresses
    - eyewear
    - footwear
    - hats
    - leggings
    - outerwear
    - pants
    - skirts
    - tops


PHOTOS
======
Download the street and shop photos from the following link:
http://tlberg.cs.unc.edu/wheretobuyit_release/photos.tar


META DATA
=========
Download the meta data from the following link:
http://tlberg.cs.unc.edu/wheretobuyit_release/meta.zip

There are three groups of files in the meta data:

TEST_PAIRS_{CATEGORY}
=====================
Contains the test split of exact street2shop pairs. Each sample consists of a street photo, the bounding box location of the clothing item and its corresponding clothing product.

TRAIN_PAIRS_{CATEGORY}
======================
Contains the train split of exact street2shop pairs. Each sample consists of a street photo, the bounding box location of the clothing item and its corresponding clothing product.

RETRIEVAL_{CATEGORY}
====================
Contains the retrieval set for each category. Note that retrieval is done within-category, i.e. the clothing label of the query is given. Every sample contains a product id and a corresponding photo id.


JSON
====
files: test_pairs_{category}.json, train_pairs_{category}.json
format: A json string containing the pairs. Every entry consists of a street photo, a bounding box, and the corresponding clothing product.

files: retrieval_{category}.json
format: A json string containing the retrieval set. Every entry consists of a product id and a corresponding photo id.


REFERENCE
=========
If you use this dataset, please cite the following paper:

M. Hadi Kiapour, Xufeng Han, Svetlana Lazebnik, Alexander C. Berg, Tamara L. Berg. Where to Buy It: Matching Street Clothing Photos in Online Shops. International Conference on Computer Vision (ICCV), 2015.