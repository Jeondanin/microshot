# microshot

  <img src="https://user-images.githubusercontent.com/39483767/84585240-b8d3fb80-ae48-11ea-9f4d-a46eb2bf1eb0.gif"> </img>

## Index
* [edge_Detection](#edge_detection)
* [skeletonization](#skeletonization)
* [node Detection](#node_detection)
* [edge Analysis](#edge_analysis)

## edge_detection
### 顕微鏡の原本写真からエッジを探知する 
Bi-Directional Cascade Networkの活用
### BDCNとは
論文によりますと、写真のエッジを探知するために大事である多数のscale representaionを双方向カスケードネットワーク構造から求められるといいます。

[Bi-Directional Cascade Network for Perceptual Edge Detection](https://arxiv.org/pdf/1902.10903.pdf)
 
  <p>
  <img width=400 src="https://user-images.githubusercontent.com/39483767/84659195-fec8b680-af51-11ea-95f9-81a0dc5d33d3.png"> </img>
   
   上記のテーブルを見ると評価メトリック（evaluation Metric）である　Average Precision (AP), Optimal Dataset Scale (ODS), Optimal Image Scale (OIS)が相当優れていることが分かります。
   
  <img width=400 src="https://user-images.githubusercontent.com/39483767/84659206-04260100-af52-11ea-8b94-2fd6029b07a8.png"> </img>
  <img width=400 src="https://user-images.githubusercontent.com/39483767/84657140-ca9fc680-af4e-11ea-83e5-ef79c02a56a7.png"> </img>
  <br>
  データセットから得られた写真結果。
  </p>
  　
  
### 顕微鏡の写真への導入
  <p align="center">
    <img src="https://user-images.githubusercontent.com/39483767/78030503-2a99be80-739d-11ea-8cae-d0fa1dd2f98a.jpg"> </img>
    <img src="https://user-images.githubusercontent.com/39483767/84375038-ea1ab480-ac19-11ea-9473-e3417e88dcd3.jpg"> </img>
  </p>

## skeletonization
### 血管構造をskeletonizeする
  <p align="center">
    <img src="https://user-images.githubusercontent.com/39483767/78030503-2a99be80-739d-11ea-8cae-d0fa1dd2f98a.jpg"> </img>
    <img src="https://user-images.githubusercontent.com/39483767/84374677-4f21da80-ac19-11ea-9aba-ff9419018e1e.png"> </img>
  </p>

## node_detection
### 血管のブランチポイント（枝分かれ部位）を探知する
  <p align="center">
    <img src="https://user-images.githubusercontent.com/39483767/84374677-4f21da80-ac19-11ea-9aba-ff9419018e1e.png"> </img>
    <img src="https://user-images.githubusercontent.com/39483767/84374662-46310900-ac19-11ea-85e3-909b60fb966c.png"> </img>
  </p>

## edge_analysis
### 距離
#### 各ブランチポイントの間の距離を求める
  <p align="center">
    <img src="https://user-images.githubusercontent.com/39483767/84375353-64e3cf80-ac1a-11ea-8048-474c3d9a9b2b.png"> </img>
    <img src="https://user-images.githubusercontent.com/39483767/84375089-fe5eb180-ac19-11ea-821d-b21f2bd5a758.png"> </img>
  </p>

