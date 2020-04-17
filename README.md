# COVID-19 CT Segmentation Challenge: Towards Efficient COVID-19 CT Annotation
A Benchmark for Lung and Infection Segmentation in COVID-19 CT scans

## Motivation

Tremendous [studies](https://github.com/HzFu/COVID19_imaging_AI_paper_list) show that  deep learning have potential for providing accurate and quantitative assessment of COVID-19 infection in CT images if hundreds  well-labeled training cases are available. However, manual delineation is time-consuming and labor-intensive. Thus, we set up this challenge to explore annotation-efficient methods for COVID-19 CT segmentation.

- How should we learn with a few training cases? 
- Can we use existing lung CT labels to assist annotation?

## Datasets

| Dataset                                                      | DESCRIPTION                                                  |
| ------------------------------------------------------------ | :----------------------------------------------------------- |
| [StructSeg 2019](https://structseg2019.grand-challenge.org/) | 50 lung CT scans; Annotations include left lung, right lung, spinal cord, esophagus, heart, trachea and gross target volume of lung cancer. |
| [NSCLC](https://wiki.cancerimagingarchive.net/display/DOI/Thoracic+Volume+and+Pleural+Effusion+Segmentations+in+Diseased+Lungs+for+Benchmarking+Chest+CT+Processing+Pipelines#7c5a8c0c0cef44e488b824bd7de60428) | 402 lung CT scans; Annotations include left lung, right lung and pleural effusion (78 cases). |
| [MSD Lung Tumor](http://medicaldecathlon.com/)               | 63 lung CT scans; Annotations include lung cancer.           |
| [COVID-CT-Seg]()                                             | 20 lung CT scans from; Annotations include left lung, right lung and infections. |



## Challenge Task 1: Learning with a few annotations

| Seg\. Task         | Training and Testing     |
| ------------------ | ------------------------ |
| Lung               | 5\-fold cross validation |
| Infection          |                          |
| Lung and infection |                          |





## Challenge Task 2: Learning with existing annotations







## Challenge Task 3: Domain Generalization




