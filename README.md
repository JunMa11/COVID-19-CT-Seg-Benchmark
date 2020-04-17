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

- task200_StructSegLung_datasplit.pkl
- task201_NSCLCLung_datasplit.pkl
- task202_MSDLungTumor_datasplit.pkl
- task203_StructSegTumor_datasplit.pkl
- task204_NSCLCPE_datasplit.pkl

## Challenge Task 3: Learning with existing annotations

- task300_
- task301_
... similar to task2










