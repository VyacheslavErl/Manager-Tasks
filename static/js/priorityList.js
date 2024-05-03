


let Buttons = document.querySelectorAll("#priorityCircle")
let WrapperButtons = document.querySelector("#page-title-priority")

let activeButton = document.querySelector('.active');
let inputClass = 'name'
let  inputName  = document.querySelector(`.${inputClass}`);






activeButton.addEventListener('mouseenter', ()=> {

  WrapperButtons.classList.remove('page-title-priority-hide')
  WrapperButtons.classList.add('page-title-priority-active')

})
WrapperButtons.addEventListener('mouseleave', ()=> {

  WrapperButtons.classList.remove('page-title-priority-active')
  WrapperButtons.classList.add('page-title-priority-hide')
  })







    Buttons.forEach(Button => Button.addEventListener('click', ()=> {



        inputName.classList.remove(...[...inputName.classList].filter(n => n !== `${inputClass}`));

if (Button.value !== 'priorityWhite') {
  let className =   Button.getAttribute('priorityValue')
    inputName.classList.add(`${className}`)
}

WrapperButtons.classList.remove('page-title-priority-active')
WrapperButtons.classList.add('page-title-priority-hide')

Button.parentNode.insertBefore(Button, activeButton);
activeButton.classList.remove('active')
Button.classList.add('active')
 
activeButton = document.querySelector('.active');   
activeButton.addEventListener('mouseenter', ()=> {

WrapperButtons.classList.remove('page-title-priority-hide')
WrapperButtons.classList.add('page-title-priority-active')

})



    }))