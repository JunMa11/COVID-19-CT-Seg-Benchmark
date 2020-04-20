# COVID-19 CT Segmentation Benchmark: Towards Efficient COVID-19 CT Annotation (Under Construction)
A Benchmark for Lung and Infection Segmentation in COVID-19 CT scans 

- Task 1: Learning with a limited annotations
- Task 2: Learning to segment COVID-19 CT scans from non-COVID-19 CT scans
- Task 3: Learning with both COVID-19 and non-COVID-19 CT scans


## Motivation

Tremendous [studies](https://github.com/HzFu/COVID19_imaging_AI_paper_list) show that  deep learning methods have potential for providing accurate and quantitative assessment of COVID-19 infection in CT scans if hundreds of well-labeled training cases are available. However, manual delineation of lung and infection is time-consuming and labor-intensive. Thus, we set up this benchmark to explore annotation-efficient methods for COVID-19 CT scans segmentation. In particular, we focus on learning to segment left lung, right lung and infection using

- pure but limited COVID-19 CT scans;

- existing labeled lung CT dataset from other non-COVID-19 lung diseases;
- heterogeneous datasets include both COVID-19 and non-COVID-19 CT scans.


## Datasets

| Dataset                                                      | DESCRIPTION                                                  | License |
| ------------------------------------------------------------ | :----------------------------------------------------------- | ------- |
| [StructSeg 2019](https://structseg2019.grand-challenge.org/) | 50 lung CT scans; Annotations include left lung, right lung, spinal cord, esophagus, heart, trachea and gross target volume of lung cancer. |Hold by the [challenge organizers](https://structseg2019.grand-challenge.org/Download/)    |
| [NSCLC](https://wiki.cancerimagingarchive.net/display/DOI/Thoracic+Volume+and+Pleural+Effusion+Segmentations+in+Diseased+Lungs+for+Benchmarking+Chest+CT+Processing+Pipelines#7c5a8c0c0cef44e488b824bd7de60428) | 402 lung CT scans; Annotations include left lung, right lung and pleural effusion (78 cases). |Creative Commons Attribution 3.0 Unported License  |
| [MSD Lung Tumor](http://medicaldecathlon.com/)               | 63 lung CT scans; Annotations include lung cancer.           |CC BY-SA        |
| [COVID-19-CT-Seg](https://zenodo.org/record/3757476#.Xpz8OcgzZPY)                                          | 20 lung CT scans from; Annotations include left lung, right lung and infections. |CC BY-NC-SA   |

![Examples](https://github.com/JunMa11/COVID-19-CT-Seg-Benchmark/blob/master/utils/ImageExamples.png)

## Segmentation Task 1: Learning with a limited annotations

> This task is based on the COVID-19-CT-Seg dataset with 20 cases. Three subtasks are to segment lung, infection or both of them. For each task, 5-fold cross-validation results should be reported. 
>
> It should be noted that each fold only has 4 training cases, and remained 16 cases are used for testing. In other words, this is a few-shot or zero-shot segmentation task. [Here](https://github.com/JunMa11/COVID-19-CT-Seg-Benchmark/tree/master/Task1) is the dataset split file.



<table>
	<tr>
	    <th><center>Seg. Task</th>
	    <th><center>Training and Testing</th>  
	</tr >
<tr >
    <td>Lung</td>
    <td rowspan="3">5-fold cross validation <br/>4 cases (20% for training)<br/> 16 cases (80% for testing)</td>
<tr>
    <td>Infection</td>
</tr>
<tr>
    <td>Lung and infection</td>
</tr>
</table>

## Segmentation Task 2: Learning to segment COVID-19 CT scans from non-COVID-19 CT scans

> This task is to segment lung and infection in COVID-19 CT scans. The main difficulty is that the training set and testing set differ in data distribution. Although all the datasets are lung CT, they vary in lesion types (i.e., cancer, pleural effusion, and COVID-19), patient cohorts and imaging scanners. 
>
> It should be noted that labeled COVID-19 CT scans are not allowed to be used during training. The following table presents the details of training, validation, and testing set, and [here](https://github.com/JunMa11/COVID-19-CT-Seg-Benchmark/tree/master/Task2) is the dataset split file. (Name (Num.) denotes the dataset name and the number of cases in this dataset, e.g., StructSeg Lung (40) denotes that 40 cases in StructSeg dataset are used for training.)



<table>
	<tr>
	    <th>Seg. Task</th>
	    <th>Training</th>
        <th>Validation</th>
        <th>(Unseen)Testing</th>
	</tr >
	<tr>
	    <td>Lung</td>
	    <td>StructSeg Lung (40) <br/>NSCLC Lung (322)</td>
        <td>StructSeg Lung (10) <br/>NSCLC Lung (80)</td>
        <td>COVID-19-CT-Seg<br/>Lung (20)</td>
	</tr>
	<tr>
	    <td>Infection</td>
	    <td>MSD Lung Tumor (51)<br/>StructSeg Gross Target (40)<br/>NSCLC Plcural Effusion (62)</td>
        <td>MSD Lung Tumor (12)<br/>StructSeg Gross Target (10)<br/>NSCLC Plcural Effusion (16)</td>
        <td>COVID-19-CT-Seg<br/>Infection(20)</td>
	</tr>
</table>



## Segmentation Task 3: Learning with both COVID-19 and non-COVID-19 CT scans

> This task is also to segment lung and infection in COVID-19 CT scans, but a limited labeled COVID-19 CT scans are allowed to be used during training. For each subtask, 5-fold cross-validation results should be reported, and [here](https://github.com/JunMa11/COVID-19-CT-Seg-Benchmark/tree/master/Task3) is the dataset split file.



<table>
    <tr>
        <th><center>Seg.Task</th>
        <th colspan="2" ><center>Training</th></td>
        <th><center>Validation</th>
        <th><center>Testing</th>
    </tr>
    <tr>
        <td><center>Lung</td>
	    <td><center>StructSeg Lung (40) <br/>NSCLC Lung (322)</td>
        <td><center>COVID-19-CT-Seg Lung(4)</td>
        <td><center>StructSeg Lung (10) <br/>NSCLC Lung (80)</td>
        <td><center>COVID-19-CT-Seg Lung(16)</td>
    </tr>
        <tr>
        <td><center>Infection</td>
        <td><center>MSD Lung Tumor (51)<br/>StructSeg Gross Target (40)<br/>NSCLC Plcural Effusion (62)</td>
        <td><center>COVID-19-CT-Seg Infection(4)</td>
        <td><center>MSD Lung Tumor (12)<br/>StructSeg Gross Target (10)<br/>NSCLC Plcural Effusion (16)</td>
        <td><center>COVID-19-CT-Seg Infection(16)</td>
    </tr>
</table>



## Guidelines

- Both semi-automatic (e.g., level set, graph cut, interactive CNN...) and fully automatic methods (e.g., CNNs...) are welcome.
-  Evaluation metrics are Dice similarity coefficient (DSC) and normalized surface Dice (NSD), and the python implementations are [here](http://medicaldecathlon.com/files/Surface_distance_based_measures.ipynb).
- For fail comparison, using additional datasets are not encouraged. 
- Ensembles by many models are not encouraged.

## TODO

- [ ] NIfTI format of NSCLC dataset
- [ ] U-Net baseline models


## Acknowledgements

We thank all the organizers of MICCAI 2018 Medical Segmentation Decathlon, MICCAI 2019 Automatic Structure Segmentation for Radiotherapy Planning Challenge, [the Coronacases Initiative](https://coronacases.org  ) and [Radiopaedia](https://radiopaedia.org/articles/covid-19-3) for the publicly available lung CT dataset. We also thank [Joseph Paul Cohen](https://github.com/ieee8023/covid-chestxray-dataset) for providing convenient download [link](https://academictorrents.com/details/136ffddd0959108becb2b3a86630bec049fcb0ff) of 20 COVID-19 CT scans. We also thank the organizers of [TMI Special Issue on Annotation-Efficient Deep Learning for Medical Imaging](http://www.embs.org/wp-content/uploads/2020/04/Special_Issue_CFP_DL4MI.pdf) because we get lots of insights from the call for papers when designing these segmentation tasks. We also thank the contributors of these great COVID-19 related resources: [COVID19_imaging_AI_paper_list](https://github.com/HzFu/COVID19_imaging_AI_paper_list) and [MedSeg](http://medicalsegmentation.com/covid19/). Last but not least, we thank Chen Chen, Xin Yang, and Yao Zhang for their important feedback on this benchmark.

