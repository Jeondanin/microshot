# microshot

  <img src="https://user-images.githubusercontent.com/39483767/84585240-b8d3fb80-ae48-11ea-9f4d-a46eb2bf1eb0.gif"> </img>

## Index
* [edge_Detection](#edge_detection)
* [skeletonization](#skeletonization)
* [node Detection](#node_detection)
* [edge Analysis](#edge_analysis)

## edge_detection
### 顕微鏡の原本写真からエッジを探知する
<br/>
  <p>Bi-Directional Cascade Networkを用いる</p>
  以下のグラフや写真は次の論文から抜粋した写真です <br>
  [論文] (https://arxiv.org/pdf/1902.10903.pdf)
 
  <p>
  <img width=400 src="https://user-images.githubusercontent.com/39483767/84657416-32561180-af4f-11ea-855f-b6e82fda9b27.png"> </img>
  <img width=400 src="https://user-images.githubusercontent.com/39483767/84657140-ca9fc680-af4e-11ea-83e5-ef79c02a56a7.png"> </img>
  </p>
  
  <p align="center">
    <img src="https://user-images.githubusercontent.com/39483767/78030503-2a99be80-739d-11ea-8cae-d0fa1dd2f98a.jpg"> </img>
    <img src="https://user-images.githubusercontent.com/39483767/84375038-ea1ab480-ac19-11ea-9473-e3417e88dcd3.jpg"> </img>
  </p>

## skeletonization
  血管構造をskeletonizeする
  <p align="center">
    <img src="https://user-images.githubusercontent.com/39483767/78030503-2a99be80-739d-11ea-8cae-d0fa1dd2f98a.jpg"> </img>
    <img src="https://user-images.githubusercontent.com/39483767/84374677-4f21da80-ac19-11ea-9aba-ff9419018e1e.png"> </img>
  </p>

## node_detection
  血管のブランチポイント（枝分かれ部位）を探知する
  <p align="center">
    <img src="https://user-images.githubusercontent.com/39483767/84374677-4f21da80-ac19-11ea-9aba-ff9419018e1e.png"> </img>
    <img src="https://user-images.githubusercontent.com/39483767/84374662-46310900-ac19-11ea-85e3-909b60fb966c.png"> </img>
  </p>

## edge_analysis
### 距離
  各ブランチポイントの間の距離を求める
  <p align="center">
    <img src="https://user-images.githubusercontent.com/39483767/84375353-64e3cf80-ac1a-11ea-8048-474c3d9a9b2b.png"> </img>
    <img src="https://user-images.githubusercontent.com/39483767/84375089-fe5eb180-ac19-11ea-821d-b21f2bd5a758.png"> </img>
  </p>

