# COVID-19 CT Segmentation Challenge: Towards Efficient COVID-19 CT Annotation
A Benchmark for Lung and Infection Segmentation in COVID-19 CT scans

## Motivation

Tremendous [studies](https://github.com/HzFu/COVID19_imaging_AI_paper_list) show that  deep learning have potential for providing accurate and quantitative assessment of COVID-19 infection in CT images if hundreds  well-labeled training cases are available. However, manual delineation is time-consuming and labor-intensive. Thus, we set up this challenge to explore annotation-efficient methods for COVID-19 CT segmentation. In particular, we focus on:

- How should we learn with a few training cases? 
- Can we use existing lung CT labels to assist annotation?

## Datasets

| Dataset                                                      | DESCRIPTION                                                  |
| ------------------------------------------------------------ | :----------------------------------------------------------- |
| [StructSeg 2019](https://structseg2019.grand-challenge.org/) | 50 lung CT scans; Annotations include left lung, right lung, spinal cord, esophagus, heart, trachea and gross target volume of lung cancer. |
| [NSCLC](https://wiki.cancerimagingarchive.net/display/DOI/Thoracic+Volume+and+Pleural+Effusion+Segmentations+in+Diseased+Lungs+for+Benchmarking+Chest+CT+Processing+Pipelines#7c5a8c0c0cef44e488b824bd7de60428) | 402 lung CT scans; Annotations include left lung, right lung and pleural effusion (78 cases). |
| [MSD Lung Tumor](http://medicaldecathlon.com/)               | 63 lung CT scans; Annotations include lung cancer.           |
| [COVID-19-CT-Seg]()                                          | 20 lung CT scans from; Annotations include left lung, right lung and infections. |


## Challenge Task 1: Learning with a few annotations

> This task is based on COVID-19-CT-Seg dataset with 20 cases. Three subtasks aim to segment lung, infection or both of them. For each task, 5-fold cross validation results should be reported. It should be noted that each fold only has 4 training cases, and remained 16 cases are used for testing. [Here]() is the dataset split file.



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

## Challenge Task 2: Domain generalization

> This task aims to segment lung and infection in COVID-19 CT scans. The main difficulty is that the training set and testing set differ significantly in data distribution, due to varying patient cohorts and imaging scanners. It should be noted that labeled COVID-19 CT scans are not allowed to be used during training. Following table presents the details of training, validation and testing set, and [here]() is the dataset split file. (Name (Num.) denotes the dataset name and the number of cases in this dataset, e.g., StructSeg Lung (40) denotes that 40 cases in StructSeg dataset are used for training.)



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



## Challenge Task 3: Learning with existing annotations

> This task also aims to segment lung and infection in COVID-19 CT scans, but a few labeled COVID-19 CT scans are allowed to be used during training. For each subtask, 5-fold cross validation result should be reported, and [here]() is the dataset split file.



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

- Teams may choose whether to participate only in a single or multiple sub-tasks or in all tasks. Each task can be evaluated separately.
- Both semi-automatic and fully automatic methods are allowed.
-  Evaluation metrics are Dice similarity coefficient (DSC) and normalized surface Dice (NSD), and the python implementations are [here](http://medicaldecathlon.com/files/Surface_distance_based_measures.ipynb).
- Life cycle type: open call.



