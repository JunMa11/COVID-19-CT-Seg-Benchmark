# Task 1: Learning with limited annotations

## 3D U-Net baselines for individual lung and infection segmentation

<table>
<tr>
    <th rowspan="3" align="left">Subtask<br/>
    <th colspan="4"><center>Lung</td>
    <th colspan="2" rowspan="2"><center>Infection</td>
</tr>
<tr>
    <th colspan="2"><center>Left Lung</td>
    <th colspan="2"><center>Right Lung</td>
</tr>
<tr>
    <th><center>DSC</td>
    <th><center>NSD</td>
    <th><center>DSC</td>
    <th><center>NSD</td>
    <th><center>DSC</td>
    <th><center>NSD</td>
</tr>
<tr>
    <th align="left">Fold0</td>
    <td><center>0.8488±0.08242</td>
    <td><center>0.6869±0.1329</td>
    <td><center>0.8521±0.1299</td>
    <td><center>0.7055±0.1578</td>
    <td><center>0.6808±0.2049</td>
    <td><center>0.7088±0.2130</td>
</tr>
<tr>
    <th align="left">Fold1</td>
    <td><center>0.8028±0.1454</td>
    <td><center>0.6182±0.1510</td>
    <td><center>0.8388±0.09582</td>
    <td><center>0.6825±0.09003</td>
    <td><center>0.7132±0.2053</td>
    <td><center>0.7182±0.2296</td>
</tr>
<tr>
    <th align="left">Fold2</td>
    <td><center>0.8714±0.1213</td>
    <td><center>0.7434±0.1595</td>
    <td><center>0.9034±0.08237</td>
    <td><center>0.7845±0.1195</td>
    <td><center>0.6618±0.2168</td>
    <td><center>0.7171±0.2415</td>
</tr>
<tr>
    <th align="left">Fold3</td>
    <td><center>0.8844±0.07027</td>
    <td><center>0.7518±0.08787</td>
    <td><center>0.8986±0.06260</td>
    <td><center>0.7845±0.07952</td>
    <td><center>0.6813±0.231</td>
    <td><center>0.7084±0.2706</td>
</tr>
<tr>
    <th align="left">Fold4</td>
    <td><center>0.8833±0.7597</td>
    <td><center>0.7583±0.1104</td>
    <td><center>0.9022±0.06963</td>
    <td><center>0.7831±0.1020</td>
    <td><center>0.6267±0.2689</td>
    <td><center>0.6493±0.2823</td>
</tr> 
<tr>
    <th align="left">Avg</td>
    <td><center>0.8582±0.1052</td>
    <td><center>0.7117±0.1384</td>
    <td><center>0.8790±0.09315</td>
    <td><center>0.7480±0.1191</td>
    <td><center>0.6728±0.2227</td>
    <td><center>0.7004±0.2437</td>
</tr>        
</table>


## 3D U-Net baselines for joint lung and infection segmentation

<table>
<tr>
    <th rowspan="3" align="left">Subtask<br/>
    <th colspan="6"><center>Lung and Infection</td>
</tr>
<tr>
    <th colspan="2"><center>Left Lung</td>
    <th colspan="2"><center>Right Lung</td>
    <th colspan="2"><center>Infection</td>
</tr>
<tr>
    <th><center>DSC</td>
    <th><center>NSD</td>
    <th><center>DSC</td>
    <th><center>NSD</td>
    <th><center>DSC</td>
    <th><center>NSD</td>
</tr>
<tr>
    <th align="left">Fold0</td>
    <td><center>0.5376±0.284</td>
    <td><center>0.3905±0.1832</td>
    <td><center>0.6547±0.1936</td>
    <td><center>0.4736±0.1426</td>
    <td><center>0.6543±0.2388</td>
    <td><center>0.6815±0.232</td>
</tr>
<tr>
    <th align="left">Fold1</td>
    <td><center>0.4031±0.1871</td>
    <td><center>0.2753±0.1198</td>
    <td><center>0.6014±0.1112</td>
    <td><center>0.4171±0.0994</td>
    <td><center>0.6471±0.2183</td>
    <td><center>0.6055±0.2511</td>
</tr>
<tr>
    <th align="left">Fold2</td>
    <td><center>0.8032±0.1875</td>
    <td><center>0.6679±0.1884</td>
    <td><center>0.8521±0.1243</td>
    <td><center>0.6862±0.1506</td>
    <td><center>0.6069±0.276</td>
    <td><center>0.6245±0.289</td>
</tr>
<tr>
    <th align="left">Fold3</td>
    <td><center>0.7965±0.1360</td>
    <td><center>0.6543±0.1442</td>
    <td><center>0.8401±0.0977</td>
    <td><center>0.6770±0.1304</td>
    <td><center>0.6198±0.2787</td>
    <td><center>0.6532±0.2891</td>
</tr>
<tr>
    <th align="left">Fold4</td>
    <td><center>0.7242±0.2109</td>
    <td><center>0.5855±0.2081</td>
    <td><center>0.8086±0.1344</td>
    <td><center>0.6340±0.1586</td>
    <td><center>0.5138±0.3015</td>
    <td><center>0.5186±0.3101</td>
</tr> 
<tr>
    <th align="left">Avg</td>
    <td><center>0.6544±0.2556</td>
    <td><center>0.5163±0.2291</td>
    <td><center>0.7527±0.1678</td>
    <td><center>0.5789±0.1746</td>
    <td><center>0.6078±0.2628</td>
    <td><center>0.6159±0.2748</td>
</tr>        
</table>



## 3D U-Net baselines for infection segmentation、 joint lung and infection segmentation(80%training,20%testing)
<table>
<tr>
    <th rowspan="3"><center>Subtask<br/>
    <th colspan="2" rowspan="2"><center>Infection</td>
    <th colspan="6"><center>Lung and Infection</td>
</tr>
<tr>
    <th colspan="2"><center>Left Lung</td>
    <th colspan="2"><center>Right Lung</td>
    <th colspan="2"><center>Infection</td>
</tr>
<tr>
    <th><center>DSC</td>
    <th><center>NSD</td>
    <th><center>DSC</td>
    <th><center>NSD</td>
    <th><center>DSC</td>
    <th><center>NSD</td>
    <th><center>DSC</td>
    <th><center>NSD</td>
</tr>
<tr>
    <th><center>Fold0</td>
    <td><center>0.8019±0.0603</td>
    <td><center>0.8599±0.09182</td>
    <td><center>0.9207±0.08202</td>
    <td><center>0.8028±0.1474</td>
    <td><center>0.9355±0.05415</td>
    <td><center>0.8018±0.1208</td>
    <td><center>0.7919±0.06362</td>
    <td><center>0.8471±0.09475</td>
</tr>
<tr>
    <th><center>Fold1</td>
    <td><center>0.7807±0.05981</td>
    <td><center>0.8358±0.07287</td>
    <td><center>0.9387±0.08439</td>
    <td><center>0.8419±0.1574</td>
    <td><center>0.9411±0.06709</td>
    <td><center>0.8192±0.1406</td>
    <td><center>0.8044±0.04674</td>
    <td><center>0.8581±0.05861</td>
</tr>
<tr>
    <th><center>Fold2</td>
    <td><center>0.8289±0.06594</td>
    <td><center>0.8602±0.04390</td>
    <td><center>0.9362±0.02470</td>
    <td><center>0.7909±0.04488</td>
    <td><center>0.9452±0.01671</td>
    <td><center>0.8016±0.03551</td>
    <td><center>0.8106±0.07865</td>
    <td><center>0.8286±0.1029</td>
</tr>
<tr>
    <th><center>Fold3</td>
    <td><center>0.8155±0.08941</td>
    <td><center>0.7971±0.1656</td>
    <td><center>0.7995±0.2199</td>
    <td><center>0.6781±0.2224</td>
    <td><center>0.8168±0.2201</td>
    <td><center>0.6834±0.2137</td>
    <td><center>0.8013±0.09603</td>
    <td><center>0.7883±0.1687</td>
</tr>
<tr>
    <th><center>Fold4</td>
    <td><center>0.6575±0.4195</td>
    <td><center>0.6886±0.4232</td>
    <td><center>0.9604±0.02932</td>
    <td><center>0.8583±0.05223</td>
    <td><center>0.9694±0.01188</td>
    <td><center>0.8556±0.009157</td>
    <td><center>0.6533±0.4286</td>
    <td><center>0.6852±0.4376</td>
</tr> 
<tr>
    <th><center>Avg</td>
    <td><center>0.7769±0.1868</td>
    <td><center>0.8083±0.1985</td>
    <td><center>0.9111±0.1162</td>
    <td><center>0.7944±0.1418</td>
    <td><center>0.9216±0.1092</td>
    <td><center>0.7923±0.1280</td>
    <td><center>0.7723±0.1902</td>
    <td><center>0.8015±0.2062</td>
</tr>        
</table>
