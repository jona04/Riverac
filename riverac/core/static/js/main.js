$(function(){

    $('.slide-principal').slick({  
        autoplay: true,
        autoplaySpeed: 4000,
        dots: true,
        infinite: true,
    });
      
    $('.slide-elenco').slick({    
        dots: true,
      infinite: true,
      autoplay: true,
      autoplaySpeed: 2000,
      speed: 300,
      slidesToShow: 3,
      slidesToScroll: 1,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
        // You can unslick at a given breakpoint now by adding:
        // settings: "unslick"
        // instead of a settings object
      ]
    });
    
    
    $('.slide-canal-galo').slick({    
        dots: true,
      infinite: false,
      speed: 300,
      slidesToShow: 3,
      slidesToScroll: 1,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
        // You can unslick at a given breakpoint now by adding:
        // settings: "unslick"
        // instead of a settings object
      ]
    });
    
    $("#modal01").modal("show");
    
    /*$('#btn_menu').click(function(){
        $('#menu-navegacao').animate({height:'250px'}, 500);
    });*/
    
    $('.nome_imagem_video').on('click', function(ev) {
        
        var end_video = ($(this).attr('name'));
        
        $("#video_principal_canal")[0].src = end_video + "&autoplay=1";
        ev.preventDefault();

    });
    
    //clica no menu e é feito scroll automatico ate o conteudo
    $('a[href*=#]:not([href=#])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
          if (target.length) {
            $('html,body').animate({
              scrollTop: target.offset().top
            }, 1000);
            return false;
          }
        }
    });
    


});

//faz a logo topo desaparecer no sroll
/*
var logo = $("#img_logo");
logo.hide();
$(window).scroll(function(){
  //more then or equals to
  if($(window).scrollTop() >= 180 ){
       logo.fadeIn("slow");
  //less then 100px from top
  } else {
      logo.hide();
  }
});
*/
