<p align="center">

  <h2 align="center"><b>CaesarNeRF</b>: Calibrated Semantic Representation for Few-shot Generalizable Neural Rendering</h2>
  <p align="center">
    <a style="text-decoration:none" href="https://haidongz-usc.github.io/">
                        Haidong Zhu</a><sup>1,*</sup>
    ·  
    <a style="text-decoration:none" href="https://www.tianyuding.com/">
                        Tianyu Ding</a><sup>2,*,&dagger;</sup>
    ·
    <a style="text-decoration:none" href="https://scholar.google.com/citations?user=2BahjdkAAAAJ&hl=en">
                       Tianyi Chen</a><sup>2</sup>
    ·
    <a style="text-decoration:none" href="https://www.microsoft.com/applied-sciences/people/ilya-zharkov">
                    Ilya Zharkov</a><sup>2</sup>
    ·
    <a style="text-decoration:none" href="https://sites.usc.edu/iris-cvlab/professor-ram-nevatia/">
                     Ram Nevatia</a><sup>1</sup>
    ·
    <a style="text-decoration:none" href="https://sites.google.com/site/lumingliangshomepage/">
                     Luming Liang</a><sup>2,&dagger;</sup>
    <br>
    <sup>1</sup>University of Southern California &nbsp;&nbsp;&nbsp; <sup>2</sup>Microsoft
    <br>
    </br>
  </p>
    </p>
<div align="center">
  <img src="./teaser.png" alt=""padding-top: 15px; margin-bottom: -3px;">Novel view synthesis for novel scenes using <span style="color: #FF0000;"><strong>ONE</strong></span> reference view on Shiny, LLFF, and MVImgNet (top to bottom).
          Each pair of images corresponds to the results from GNT (left) and CaesarNeRF (right).</p>
</div>

Generalizability and few-shot learning are key challenges in Neural Radiance Fields (NeRF), often due to the lack of a holistic understanding in pixel-level rendering. We introduce CaesarNeRF, an end-to-end approach that leverages scene-level <strong>CA</strong>librat<strong>E</strong>d <strong>S</strong>em<strong>A</strong>ntic <strong>R</strong>epresentation along with pixel-level representations to advance few-shot, generalizable neural rendering, facilitating a holistic understanding without compromising high-quality details. CaesarNeRF explicitly models pose differences of reference views to combine scene-level semantic representations, providing a calibrated holistic understanding. This calibration process aligns various viewpoints with precise location and is further enhanced by sequential refinement to capture varying details. Extensive experiments on public datasets, including LLFF, Shiny, mip-NeRF 360, and MVImgNet, show that CaesarNeRF delivers state-of-the-art performance across varying numbers of reference views, proving effective even with a single reference image.
 
## Citing
If you find our work helpful, please feel free to use the following BibTex entry:
```BibTeX
@article{TODO,<br>
    author = {TODO},
    title  = {TODO},
    joural = {ArXiv},
    year   = {2023},
}
```