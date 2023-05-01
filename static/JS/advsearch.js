const catTitle = document.querySelectorAll('.cat-title');
const allCatPosts = document.querySelectorAll('.all');

for(let i = 0; i < catTitle.length; i++){
  catTitle[i].addEventListener('click',filterPosts.bind(this, catTitle[i]));

}

function filterPosts(item){
  changeActivePosition(item);
  for(let i = 0; i < allCatPosts.length; i++){
    if(allCatPosts[i].classList.contains(item.attributes.id.value)){
      allCatPosts[i].style.display = "block";
    }
    else{
      allCatPosts[i].style.display = "none";
    }
  }
}

function changeActivePosition(activateItem){
  for(let i = 0; i < catTitle.length; i++){
    catTitle[i].classList.remove('active');
  }
  activateItem.classList.add('active');
};