function loco(){
    gsap.registerPlugin(ScrollTrigger);

const locoScroll = new LocomotiveScroll({
  el: document.querySelector("#main"),
  smooth: true
});
locoScroll.on("scroll", ScrollTrigger.update);

ScrollTrigger.scrollerProxy("#main", {
  scrollTop(value) {
    return arguments.length ? locoScroll.scrollTo(value, 0, 0) : locoScroll.scroll.instance.scroll.y;
  }, 
  getBoundingClientRect() {
    return {top: 0, left: 0, width: window.innerWidth, height: window.innerHeight};
  },

  pinType: document.querySelector("#main").style.transform ? "transform" : "fixed"
});
 
ScrollTrigger.addEventListener("refresh", () => locoScroll.update());

ScrollTrigger.refresh();

}
loco()
const container = document.querySelector('.container');
const element = document.querySelector('.d-element');

// gsap.to(container, {
//             scrollTrigger: {
//                 trigger: container,
//                 start: 'top top',
//                 end: '+=300%', // Adjust the duration based on your requirements
//                 scrub: 1,
//             },
//             y: 900, // Adjust the scroll distance based on your requirements
//         });


// gsap.to(element, {
//     scrollTrigger: {
//         trigger: container,
//         start: 'top top',
//         end: 'bottom bottom',
//         scrub: 1,
//     },

//     z: -500, // Adjust the depth based on your requirements
//     x: -200, // Adjust the left movement based on your requirements
// });

// function page2Animation(){
//   gsap.from("#infotxt",{
//       y: 120,
//       stagger :0.25,
//       duration: 1,
//       scrollTrigger: {
//       trigger: "#infotxt" ,
//       scroller: ".cob-txt" ,
//       start: "top 5%",
//       end:"top 37%" ,

//       scrub: 2
//       }
//     });

// }
// page2Animation()



var tl=gsap.timeline()

tl.from("#loader h3",{
  x:40,
  opacity:0,
  duration:1,
  stagger:0.1
})
tl.to("#loader h3",{
  opacity:0,
  x:-10,
  duration:1,
  stagger:0.1
})

tl.to("#loader",{
  opacity:0
})
tl.to("#loader",{
  display:"none"
})
tl.from("#cob1 h1 span",{
  y:50,
  opacity:0,
  stagger:0.09,
  duration:1.5,
  delay:-1,
  ease: "power3.out",
})






gsap.registerPlugin(ScrollTrigger);

// Create a GSAP timeline
var tl = gsap.timeline({
  scrollTrigger: {
    trigger: "#trigger", // ID of the trigger element
    start: "top top", // Trigger the animation when the top of the trigger element reaches the top of the viewport
    end: "bottom bottom", // End the animation when the bottom of the trigger element reaches the bottom of the viewport
    toggleActions: "play none none none" // Play the animation when entering the trigger area
  }
});

// Animation code for the span element
tl.from("#trigger", { y: -100, opacity: 0, duration: 1, ease: "power3.out" });

// Show the span element when the scroll reaches the bottom
tl.set("#trigger", { display: "block" });







// document.querySelector(".ftext")
// .addEventListener("mouseover", function(){
//   gsap.to("#future video"),{
//     opacity:1,
//     duration:1.5,
//     ease: Power4
//   }
// })
// document.querySelector(".ftext")
// .addEventListener("mouseleave", function(){
//   gsap.from("#future video"),{
//     opacity:0,
//     duration:1.5,
//     ease: Power4
//   }
// })

// Selecting the element with class "ftext"
var ftextElement = document.querySelector(".ftext");

// Adding mouseover event listener
ftextElement.addEventListener("mouseover", function() {
  // Selecting the video element with the id "future"
  var futureVideo = document.getElementById("ad");

 
  // Setting the opacity to 1 with a duration of 1.5 seconds
  futureVideo.style.opacity = 1;
  futureVideo.style.transition = "opacity 1.5s ease";
  
});

// Adding mouseleave event listener
ftextElement.addEventListener("mouseleave", function() {
  // Selecting the video element with the id "future"
  var futureVideo = document.getElementById("ad");

  // Setting the opacity to 0 with a duration of 1.5 seconds
  futureVideo.style.opacity = 0;
  futureVideo.style.transition = "opacity 1.5s ease";
});

























// for cursor
// var page1Content =document.querySelector("page1-content")
// var cursor=Document.querySelector("cursor")

// page1Content.addEventListener("mousemove",function(dets){
//   gsap.to(cursor,{
//       x:dets.x,
//       y:dets.y
//   })
// })
