from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import RedirectView, TemplateView
from bs4 import BeautifulSoup

def load(request):
    html = """
<!DOCTYPE html>
<html lang="en" class="no-js">
<!-- Begin Head -->

<head>
    <!-- Basic -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Rrosetta</title>
    <meta name="keywords" content="Rrosetta" />
    <meta name="description" content="by Free Wifi">
    <meta name="author" content="melnycz.uk">

    <!-- Web Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Lato:300,400,400i|Montserrat:400,700" rel="stylesheet">

    <!-- Vendor Styles -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <link href="css/animate.css" rel="stylesheet" type="text/css" />
    <link href="vendor/themify/themify.css" rel="stylesheet" type="text/css" />
    <link href="vendor/scrollbar/scrollbar.min.css" rel="stylesheet" type="text/css" />
    <link href="vendor/magnific-popup/magnific-popup.css" rel="stylesheet" type="text/css" />
    <link href="vendor/swiper/swiper.min.css" rel="stylesheet" type="text/css" />
    <link href="vendor/cubeportfolio/css/cubeportfolio.min.css" rel="stylesheet" type="text/css" />

    <!-- Theme Styles -->
    <link href="css/style.css" rel="stylesheet" type="text/css" />
    <link href="css/global/global.css" rel="stylesheet" type="text/css" />

    <!-- Favicon -->
    <link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">
    <link rel="apple-touch-icon" href="img/apple-touch-icon.png">
</head>
<!-- End Head -->

<!-- Body -->

<body>

    <!--========== HEADER ==========-->
    <header class="navbar-fixed-top s-header js__header-sticky js__header-overlay">
        <!-- Navbar -->
        <div class="s-header__navbar">
            <div class="s-header__container">
                <div class="s-header__navbar-row">
                    <div class="s-header__navbar-row-col">
                        <!-- Logo -->
                        <div class="s-header__logo">
                            <a href="index.html" class="s-header__logo-link">
                                <!-- <img class="s-header__logo-img s-header__logo-img-default" src="img/logo.png" alt="Megakit Logo"> -->
                                <!-- <img class="s-header__logo-img s-header__logo-img-shrink" src="img/logo-dark.png" alt="Megakit Logo"> -->
                                <p><i>FREE WIFI PRESS</i></p>
                            </a>
                        </div>
                        <!-- End Logo -->
                    </div>
                </div>
            </div>
        </div>
        <!-- End Navbar -->
    </header>
    <!--========== END HEADER ==========-->

    <!--========== SWIPER SLIDER ==========-->
    <!-- <div class="s-swiper js__swiper-one-item">
        Swiper Wrapper
        <div class="swiper-wrapper">
            <div class="g-fullheight--xs g-bg-position--center swiper-slide" style="background: url('img/1920x1080/02.jpg');">
                <div class="container g-text-center--xs g-ver-center--xs">
                    <div class="g-margin-b-30--xs">
                        
                        </div>
                </div>
            </div>

            <a href="#js__scroll-to-section" class="s-scroll-to-section-v1--bc g-margin-b-15--xs">
                <span class="g-font-size-18--xs g-color--white ti-angle-double-down"></span>
                <p class="text-uppercase g-color--white g-letter-spacing--3 g-margin-b-0--xs">Learn More</p>
            </a>
        </div> -->
    <!--========== END SWIPER SLIDER ==========-->

    <!-- Parallax -->
    <div class="js__parallax-window" style="background: url(img/1920x1080/12.jpg) 50% 0 no-repeat fixed;">
        <div class="container g-text-center--xs g-padding-y-200--xs g-padding-y-200--sm">
            <div class="g-margin-b-80--xs">
                <h3 class="g-font-size-24--xs g-font-size-35--sm g-font-size-45--md g-color--white"><i>Introducing</i></h3>
                <h1 class="g-font-size-35--xs g-font-size-45--sm g-font-size-55--md g-color--white">Rrosetta</h1>
                <h3 class="g-font-size-24--xs g-font-size-35--sm g-font-size-45--md g-color--white"><i>the data driven zine publishing app</i></h3>
            </div>
        </div>
    </div>
    <!-- End Parallax -->

    <!--========== PAGE CONTENT ==========-->
    <!-- Features -->
    <div id="js__scroll-to-section" class="container g-padding-y-80--xs g-padding-y-125--sm">
        <div class="g-text-center--xs g-margin-b-100--xs">
            <p class="text-uppercase g-font-size-14--xs g-font-weight--700 g-color--primary g-letter-spacing--2 g-margin-b-25--xs">publishing taken from you</p>
            <h2 class="g-font-size-32--xs g-font-size-36--md">She would like to get to know you</h2>
        </div>
        <div class="row g-margin-b-60--xs g-margin-b-70--md">
            <div class="col-sm-4 g-margin-b-60--xs g-margin-b-0--md">
                <div class="clearfix">
                    <div class="g-media g-width-30--xs">
                        <div class="wow fadeInDown" data-wow-duration=".3" data-wow-delay=".1s">
                            <i class="g-font-size-28--xs g-color--primary ti-panel"></i>
                        </div>
                    </div>
                    <div class="g-media__body g-padding-x-20--xs">
                        <h3 class="g-font-size-18--xs">One of a kind</h3>
                        <p class="g-margin-b-0--xs">Every publication is unique.<br>Every publication is personal.</p>
                    </div>
                </div>
            </div>
            <div class="col-sm-4 g-margin-b-60--xs g-margin-b-0--md">
                <div class="clearfix">
                    <div class="g-media g-width-30--xs">
                        <div class="wow fadeInDown" data-wow-duration=".3" data-wow-delay=".2s">
                            <i class="g-font-size-28--xs g-color--primary ti-desktop"></i>
                        </div>
                    </div>
                    <div class="g-media__body g-padding-x-20--xs">
                        <h3 class="g-font-size-18--xs">Dig Deep</h3>
                        <p class="g-margin-b-0--xs">Rrosetta is smart.<br>She will find out all about you.</p>
                    </div>
                </div>
            </div>
            <div class="col-sm-4">
                <div class="clearfix">
                    <div class="g-media g-width-30--xs">
                        <div class="wow fadeInDown" data-wow-duration=".3" data-wow-delay=".3s">
                            <i class="g-font-size-28--xs g-color--primary ti-ruler-alt-2"></i>
                        </div>
                    </div>
                    <div class="g-media__body g-padding-x-20--xs">
                        <h3 class="g-font-size-18--xs">Yours To Own</h3>
                        <p class="g-margin-b-0--xs">Rrosetta produces a bespoke zine.<br>This is your data given back to you.</p>
                    </div>
                </div>
            </div>
        </div>
        <!-- // end row  -->
    </div>
    <!-- End Features -->



    <!-- Culture -->
    <div class="g-promo-section">
        <div class="container g-padding-y-80--xs g-padding-y-125--sm">
            <div class="row">
                <div class="col-md-4 g-margin-t-15--xs g-margin-b-60--xs g-margin-b-0--lg">
                    <p class="text-uppercase g-font-size-14--xs g-font-weight--700 g-color--primary g-letter-spacing--2 g-margin-b-25--xs">Reading your Gmail</p>
                    <div class="wow fadeInLeft" data-wow-duration=".3" data-wow-delay=".1s">
                        <h2 class="g-font-size-40--xs g-font-size-50--sm g-font-size-60--md">About</h2>
                    </div>
                    <div class="wow fadeInLeft" data-wow-duration=".3" data-wow-delay=".3s">
                        <h2 class="g-font-size-40--xs g-font-size-50--sm g-font-size-60--md">Rrosetta</h2>
                    </div>
                </div>
                <div class="col-md-4 col-md-offset-1">
                    <p class="g-font-size-18--xs">Rrosetta is an intelligent programme that learns from reading your sent emails.<br><br>By giving your consent to access your Gmail account, Rrosetta will read your emails and learn what you like to talk about.<br><br>With this data
                        she designs a small booklet full of things she thinks you'd like, and prints it autonomously.</p>
                    <p class="g-font-size-18--xs">.</p>
                </div>
            </div>
        </div>
        <div class="col-sm-3 g-promo-section__img-right--lg g-bg-position--center g-height-100-percent--md js__fullwidth-img">
            <img class="img-responsive" src="img/970x970/02.jpg" alt="Image">
        </div>
    </div>
    <!-- End Culture -->

    <!-- Subscribe -->
    <div class="js__parallax-window" style="background: url(img/1920x1080/14.jpg) 50% 0 no-repeat fixed;">
        <div class="g-container--sm g-text-center--xs g-padding-y-80--xs g-padding-y-125--sm">
            <div class="g-margin-b-80--xs">
                <p class="text-uppercase g-font-size-14--xs g-font-weight--700 g-color--white-opacity g-letter-spacing--2 g-margin-b-25--xs">Join Her</p>
                <h2 class="g-font-size-32--xs g-font-size-36--md g-color--white">Want To Begin?</h2>
            </div>
            <div class="row">
                <!-- <div class="col-sm-8 col-sm-offset-4 col-xs-10 col-xs-offset-1"> -->
                <!-- <div class="g-container--sm g-text-center--xs g-padding-y-80--xs g-padding-y-125--sm"> -->
                <div class="g-text-center--xs g-margin-b-50--xs">
                    <form method="post" action="http://rrosetta.herokuapp.com/backend">
                        <button class="s-btn s-btn-icon--md s-btn-icon--white-brd s-btn--white-brd g-radius--left-50 g-radius--right-50">Sign up with Google</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    </div>
    <!-- End Subscribe -->

    <!-- Portfolio Filter -->
    <div class="container g-padding-y-80--xs">
        <div class="g-text-center--xs g-margin-b-40--xs">
            <h2 class="g-font-size-32--xs g-font-size-36--md">Gallery</h2>
        </div>
    </div>
    <!-- End Portfolio Filter -->

    <!-- Portfolio Gallery -->
    <div class="container g-margin-b-100--xs">
        <div id="js__grid-portfolio-gallery" class="cbp">
            <!-- Item -->
            <div class="s-portfolio__item cbp-item logos motion">
                <div class="s-portfolio__img-effect">
                    <img src="img/970x647/05.jpg" alt="Portfolio Image">
                </div>
                <div class="s-portfolio__caption-hover--cc">
                    <div class="g-margin-b-25--xs">
                        <h4 class="g-font-size-18--xs g-color--white g-margin-b-5--xs">Portfolio Item</h4>
                        <p class="g-color--white-opacity">by KeenThemes Inc.</p>
                    </div>
                    <ul class="list-inline g-ul-li-lr-5--xs g-margin-b-0--xs">
                        <li>
                            <a href="img/970x647/05.jpg" class="cbp-lightbox s-icon s-icon--sm s-icon--white-bg g-radius--circle" data-title="Portfolio Item <br/> by KeenThemes Inc.">
                                <i class="ti-fullscreen"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?ref=keenthemes" class="s-icon s-icon--sm s-icon s-icon--white-bg g-radius--circle">
                                <i class="ti-link"></i>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- Item -->
            <div class="s-portfolio__item cbp-item graphic">
                <div class="s-portfolio__img-effect">
                    <img src="img/970x647/06.jpg" alt="Portfolio Image">
                </div>
                <div class="s-portfolio__caption-hover--cc">
                    <div class="g-margin-b-25--xs">
                        <h4 class="g-font-size-18--xs g-color--white g-margin-b-5--xs">Portfolio Item</h4>
                        <p class="g-color--white-opacity">by KeenThemes Inc.</p>
                    </div>
                    <ul class="list-inline g-ul-li-lr-5--xs g-margin-b-0--xs">
                        <li>
                            <a href="img/970x647/06.jpg" class="cbp-lightbox s-icon s-icon--sm s-icon--white-bg g-radius--circle" data-title="Portfolio Item <br/> by KeenThemes Inc.">
                                <i class="ti-fullscreen"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?ref=keenthemes" class="s-icon s-icon--sm s-icon s-icon--white-bg g-radius--circle">
                                <i class="ti-link"></i>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- Item -->
            <div class="s-portfolio__item cbp-item logos">
                <div class="s-portfolio__img-effect">
                    <img src="img/970x647/07.jpg" alt="Portfolio Image">
                </div>
                <div class="s-portfolio__caption-hover--cc">
                    <div class="g-margin-b-25--xs">
                        <h4 class="g-font-size-18--xs g-color--white g-margin-b-5--xs">Portfolio Item</h4>
                        <p class="g-color--white-opacity">by KeenThemes Inc.</p>
                    </div>
                    <ul class="list-inline g-ul-li-lr-5--xs g-margin-b-0--xs">
                        <li>
                            <a href="img/970x647/07.jpg" class="cbp-lightbox s-icon s-icon--sm s-icon--white-bg g-radius--circle" data-title="Portfolio Item <br/> by KeenThemes Inc.">
                                <i class="ti-fullscreen"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?ref=keenthemes" class="s-icon s-icon--sm s-icon s-icon--white-bg g-radius--circle">
                                <i class="ti-link"></i>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- Item -->
            <div class="s-portfolio__item cbp-item motion graphic">
                <div class="s-portfolio__img-effect">
                    <img src="img/970x647/08.jpg" alt="Portfolio Image">
                </div>
                <div class="s-portfolio__caption-hover--cc">
                    <div class="g-margin-b-25--xs">
                        <h4 class="g-font-size-18--xs g-color--white g-margin-b-5--xs">Portfolio Item</h4>
                        <p class="g-color--white-opacity">by KeenThemes Inc.</p>
                    </div>
                    <ul class="list-inline g-ul-li-lr-5--xs g-margin-b-0--xs">
                        <li>
                            <a href="img/970x647/08.jpg" class="cbp-lightbox s-icon s-icon--sm s-icon--white-bg g-radius--circle" data-title="Portfolio Item <br/> by KeenThemes Inc.">
                                <i class="ti-fullscreen"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?ref=keenthemes" class="s-icon s-icon--sm s-icon s-icon--white-bg g-radius--circle">
                                <i class="ti-link"></i>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- Item -->
            <div class="s-portfolio__item cbp-item logos graphic">
                <div class="s-portfolio__img-effect">
                    <img src="img/970x647/09.jpg" alt="Portfolio Image">
                </div>
                <div class="s-portfolio__caption-hover--cc">
                    <div class="g-margin-b-25--xs">
                        <h4 class="g-font-size-18--xs g-color--white g-margin-b-5--xs">Portfolio Item</h4>
                        <p class="g-color--white-opacity">by KeenThemes Inc.</p>
                    </div>
                    <ul class="list-inline g-ul-li-lr-5--xs g-margin-b-0--xs">
                        <li>
                            <a href="img/970x647/09.jpg" class="cbp-lightbox s-icon s-icon--sm s-icon--white-bg g-radius--circle" data-title="Portfolio Item <br/> by KeenThemes Inc.">
                                <i class="ti-fullscreen"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?ref=keenthemes" class="s-icon s-icon--sm s-icon s-icon--white-bg g-radius--circle">
                                <i class="ti-link"></i>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- Item -->
            <div class="s-portfolio__item cbp-item motion graphic">
                <div class="s-portfolio__img-effect">
                    <img src="img/970x647/04.jpg" alt="Portfolio Image">
                </div>
                <div class="s-portfolio__caption-hover--cc">
                    <div class="g-margin-b-25--xs">
                        <h4 class="g-font-size-18--xs g-color--white g-margin-b-5--xs">Portfolio Item</h4>
                        <p class="g-color--white-opacity">by KeenThemes Inc.</p>
                    </div>
                    <ul class="list-inline g-ul-li-lr-5--xs g-margin-b-0--xs">
                        <li>
                            <a href="img/970x647/04.jpg" class="cbp-lightbox s-icon s-icon--sm s-icon--white-bg g-radius--circle" data-title="Portfolio Item <br/> by KeenThemes Inc.">
                                <i class="ti-fullscreen"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?ref=keenthemes" class="s-icon s-icon--sm s-icon s-icon--white-bg g-radius--circle">
                                <i class="ti-link"></i>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- End Item -->
        </div>
        <!-- End Portfolio Gallery -->
    </div>
    <!-- End Portfolio -->

    <!-- Google Map -->
    <div class="container g-padding-y-80--xs">
        <div class="g-text-center--xs g-margin-b-40--xs">
            <h2 class="g-font-size-32--xs g-font-size-36--md">Where In The World Is Rrosetta?</h2>
        </div>
    </div>
    <section class="s-google-map">
        <div id="js__google-container" class="s-google-container g-height-400--xs"></div>
    </section>
    <!-- End Google Map -->
    <!--========== END PAGE CONTENT ==========-->

    <!--========== FOOTER ==========-->
    <footer class="g-bg-color--dark">
        <!-- Links -->
        <div class="g-hor-divider__dashed--white-opacity-lightest">
            <div class="container g-padding-y-50--xs" style="overflow:hidden;">
                <div class="container g-padding-y-0--xs" style="width:50%; float:left;">
                    <!-- <div class="col-sm-12 g-margin-b-20--xs g-margin-20--md"> -->
                    <h2 class="g-font-size-15--xs g-color--white-opacity">Rrosetta is an art project by Howard Melnyczuk<br>It is currently being exhibited as part of Overlap 2017</h2>
                    <!-- </div> -->
                    <div class="row">
                        <div class="col-sm-4 g-margin-b-40--xs g-margin-b-0--md">
                            <ul class="list-unstyled g-ul-li-tb-5--xs g-margin-b-0--xs">
                                <li><a class="g-font-size-15--xs g-color--white-opacity" href="http://howardmelnyczuk.co.uk">Howard Melnyczuk</a></li>
                                <li><a class="g-font-size-15--xs g-color--white-opacity" href="mailto:h.melnyczuk@gmail.com">Contact</a></li>
                                <li></li>
                                <li><a class="g-font-size-15--xs g-color--white-opacity" href="http://rrosetta.uk">Overlap</a></li>
                            </ul>
                        </div>
                        <div class="col-sm-4 g-margin-b-40--xs g-margin-b-0--md">
                            <ul class="list-unstyled g-ul-li-tb-5--xs g-margin-b-0--xs">
                                <li><a class="g-font-size-15--xs g-color--white-opacity" href="http://twitter.com/melnyczuk">Twitter</a></li>
                                <li><a class="g-font-size-15--xs g-color--white-opacity" href="http://melnyczuk.tumblr.com">Tumblr</a></li>
                                <li><a class="g-font-size-15--xs g-color--white-opacity" href="http://instagram.com/melnyczuk">Instagram</a></li>
                                <li><a class="g-font-size-15--xs g-color--white-opacity" href="https://www.youtube.com/channel/UCv6eQkf2sEF89OaVgQgJ7_w">YouTube</a></li>
                            </ul>
                        </div>
                        <div class="col-sm-4 g-margin-b-40--xs g-margin-b-0--md">
                            <ul class="list-unstyled g-ul-li-tb-5--xs g-margin-b-0--xs">
                                <li><a class="g-font-size-15--xs g-color--white-opacity" href="http://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?ref=keenthemes">Subscribe to Our Newsletter</a></li>
                                <li><a class="g-font-size-15--xs g-color--white-opacity" href="http://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?ref=keenthemes">Privacy Policy</a></li>
                                <li><a class="g-font-size-15--xs g-color--white-opacity" href="http://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?ref=keenthemes">Terms &amp; Conditions</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-md-0 col-md-offset-1 col-sm-4 col-sm-offset-1 s-footer__logo g-padding-y-0--xs g-padding-y-0--md" style="float:left">
                    <h3 class="g-font-size-18--xs g-color--white">Free Wifi</h3>
                    <p class="g-color--white-opacity">Free Wifi is an interdiscerplinary design studio founded by Howard Melnyczuk in 2015.<br><br>It also runs Free Wifi Press<br>an independent publishing house<br><br>An online gallery will be opening in 2018.</p>
                </div>
            </div>
        </div>

        <!-- End Links -->
        <!-- Copyright -->
    </footer>
    <!--==========END FOOTER==========-->
    <!-- Back To Top -->
    <a href="javascript:void(0);" class="s-back-to-top js__back-to-top"></a>
    <!--==========JAVASCRIPTS (Load javascripts at bottom, this will reduce page load time)==========-->
    <!-- Vendor -->
    <script type="text/javascript" src="vendor/jquery.min.js"></script>
    <script type="text/javascript" src="vendor/jquery.migrate.min.js"></script>
    <script type="text/javascript" src="vendor/bootstrap/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="vendor/jquery.smooth-scroll.min.js"></script>
    <script type="text/javascript" src="vendor/jquery.back-to-top.min.js"></script>
    <script type="text/javascript" src="vendor/scrollbar/jquery.scrollbar.min.js"></script>
    <script type="text/javascript" src="vendor/magnific-popup/jquery.magnific-popup.min.js"></script>
    <script type="text/javascript" src="vendor/swiper/swiper.jquery.min.js"></script>
    <script type="text/javascript" src="vendor/waypoint.min.js"></script>
    <script type="text/javascript" src="vendor/counterup.min.js"></script>
    <script type="text/javascript" src="vendor/cubeportfolio/js/jquery.cubeportfolio.min.js"></script>
    <script type="text/javascript" src="vendor/jquery.parallax.min.js"></script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBsXUGTFS09pLVdsYEE9YrO2y4IAncAO2U"></script>
    <script type="text/javascript" src="vendor/jquery.wow.min.js"></script>
    <!-- General Components and Settings -->
    <script type="text/javascript" src="js/global.min.js"></script>
    <script type="text/javascript" src="js/components/header-sticky.min.js"></script>
    <script type="text/javascript" src="js/components/scrollbar.min.js"></script>
    <script type="text/javascript" src="js/components/magnific-popup.min.js"></script>
    <script type="text/javascript" src="js/components/swiper.min.js"></script>
    <script type="text/javascript" src="js/components/counter.min.js"></script>
    <script type="text/javascript" src="js/components/portfolio-3-col.min.js"></script>
    <script type="text/javascript" src="js/components/parallax.min.js"></script>
    <script type="text/javascript" src="js/components/google-map.min.js"></script>
    <script type="text/javascript" src="js/components/wow.min.js"></script>
    <!--==========END JAVASCRIPTS==========-->
</body>
<!-- End Body -->

</html>
    """
    return HttpResponse(html)