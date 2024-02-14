const form = document.querySelector('#form');
const taskInput = document.querySelector('#taskInput');
const tasksList = document.querySelector('#tasksList');
form.addEventListener('submit',function(event){
    event.preventDefault();

    const taskText=taskInput.value;

    

    const taskHTML = `<li class="elem">
    <button data-action="done" class="btn2 check"></button> 
    <span class="text" >${taskText}</span>
    <button data-action="delete" class="btn3 check"></button>
    
    </li>`;
    tasksList.insertAdjacentHTML("beforeend",taskHTML);
    taskText=taskInput.value="";
})

tasksList.addEventListener('click',deleteTask)

function deleteTask(event){
    if(event.target.dataset.action === 'delete'){
        const parenNode = event.target.closest('.elem');
        parenNode.remove();
    }
}

tasksList.addEventListener('click',doneTask)

function doneTask(event){
    if(event.target.dataset.action === 'done'){
        const parenNode = event.target.closest('.elem');
        const taskTitle = parenNode.querySelector('.text')
        const taskTitle2 = parenNode.querySelector('.btn2')
        taskTitle.classList.toggle('text-title--done');
        taskTitle2.classList.toggle('btn-done');
    }
}