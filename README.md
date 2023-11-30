<p align="center">

  <h2 align="center"><b>CaesarNeRF</b>: Calibrated Semantic Representation <br>for Few-shot Generalizable Neural Rendering</h2>
  <p align="center">
    <a style="text-decoration:none" href="https://haidongz-usc.github.io/">
                        Haidong Zhu</a><sup>1,*</sup>
    &nbsp;&nbsp;
    <a style="text-decoration:none" href="https://www.tianyuding.com/">
                        Tianyu Ding</a><sup>2,*,&dagger;</sup>
    &nbsp;&nbsp;
    <a style="text-decoration:none" href="https://scholar.google.com/citations?user=2BahjdkAAAAJ&hl=en">
                       Tianyi Chen</a><sup>2</sup>
    &nbsp;&nbsp;
    <a style="text-decoration:none" href="https://www.microsoft.com/applied-sciences/people/ilya-zharkov">
                    Ilya Zharkov</a><sup>2</sup>
    &nbsp;&nbsp;
    <a style="text-decoration:none" href="https://sites.usc.edu/iris-cvlab/professor-ram-nevatia/">
                     Ram Nevatia</a><sup>1</sup>
    &nbsp;&nbsp;
    <a style="text-decoration:none" href="https://sites.google.com/site/lumingliangshomepage/">
                     Luming Liang</a><sup>2,&dagger;</sup>
    <br>
    <sup>1</sup>University of Southern California &nbsp;&nbsp;&nbsp; <sup>2</sup>Microsoft
    <br>
    </br>
  <a href="https://haidongz-usc.github.io/project/caesarnerf"><strong>Project Page</strong></a> | <a href="https://arxiv.org/abs/2311.15510"><strong>Paper</strong></a> | <a href="https://haidongz-usc.github.io/project/pdf/caesar_supp.pdf"><strong>Supplementary Material</strong></a>
  </p>
</p>
<div align="center">
  <br>
  <img src="./teaser.png" alt="<p class="text-center" style="padding-top: 15px; margin-bottom: -3px;">Novel view synthesis for novel scenes using <span><strong>ONE</strong></span> reference view on Shiny, LLFF, and MVImgNet (top to bottom). Each pair of images corresponds to the results from GNT (left) and CaesarNeRF (right).</p>
</div>

Generalizability and few-shot learning are key challenges in Neural Radiance Fields (NeRF), often due to the lack of a holistic understanding in pixel-level rendering. We introduce CaesarNeRF, an end-to-end approach that leverages scene-level <strong>CA</strong>librat<strong>E</strong>d <strong>S</strong>em<strong>A</strong>ntic <strong>R</strong>epresentation along with pixel-level representations to advance few-shot, generalizable neural rendering, facilitating a holistic understanding without compromising high-quality details. CaesarNeRF explicitly models pose differences of reference views to combine scene-level semantic representations, providing a calibrated holistic understanding. This calibration process aligns various viewpoints with precise location and is further enhanced by sequential refinement to capture varying details. Extensive experiments on public datasets, including LLFF, Shiny, mip-NeRF 360, and MVImgNet, show that CaesarNeRF delivers state-of-the-art performance across varying numbers of reference views, proving effective even with a single reference image.
 
## Citing
If you find our work helpful, please feel free to use the following BibTex entry:
```BibTeX
@article{zhu2023caesarnerf,
    author = {Zhu, Haidong and Ding, Tianyu and Chen, Tianyi and Zharkov, Ilya and Nevatia, Ram and Liang, Luming},
    title  = {CaesarNeRF: Calibrated Semantic Representation for Few-shot Generalizable Neural Rendering},
    journal={arXiv preprint arXiv:2311.15510},
    year   = {2023},
}
```