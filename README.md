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
        <td>COVID-CT-Seg<br/>Lung (20)</td>
	</tr>
	<tr>
	    <td>Infection</td>
	    <td>MSD Lung Tumor (51)<br/>StructSeg Gross Target (40)<br/>NSCLC Plcural Effusion (62)</td>
        <td>MSD Lung Tumor (12)<br/>StructSeg Gross Target (10)<br/>NSCLC Plcural Effusion (16)</td>
        <td>COVID-CT-Seg<br/>Infection(20)</td>
	</tr>
</table>

- task200_StructSegLung_datasplit.pkl
- task201_NSCLCLung_datasplit.pkl
- task202_MSDLungTumor_datasplit.pkl
- task203_StructSegTumor_datasplit.pkl
- task204_NSCLCPE_datasplit.pkl

## Challenge Task 3: Learning with existing annotations
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
        <td><center>COVID-CT-Seg Lung(4)</td>
        <td><center>StructSeg Lung (10) <br/>NSCLC Lung (80)</td>
        <td><center>COVID-CT-Seg Lung(16)</td>
    </tr>
        <tr>
        <td><center>Infection</td>
        <td><center>MSD Lung Tumor (51)<br/>StructSeg Gross Target (40)<br/>NSCLC Plcural Effusion (62)</td>
        <td><center>COVID-CT-Seg Infection(4)</td>
        <td><center>MSD Lung Tumor (12)<br/>StructSeg Gross Target (10)<br/>NSCLC Plcural Effusion (16)</td>
        <td><center>COVID-CT-Seg Infection(16)</td>
    </tr>
</table>

- task300_
- task301_
... similar to task2










