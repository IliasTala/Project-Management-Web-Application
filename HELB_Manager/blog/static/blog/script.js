const list_items = document.querySelectorAll('.list-item');
const lists = document.querySelectorAll('.list');

const userNameElement = document.querySelector('.user-connected');
const userName = userNameElement.textContent;

let draggedItem = null;


//////////////////
// DRAG & DROP  //
//////////////////
function saveDraggedItemLocation(e) {

  // empeche le comportement par defaut de l'event drop
  e.preventDefault();

  // recupere l'element de liste cible de l'event drop
  const targetList = e.target;

  // verifie que l'element drop est défini

  if (draggedItem && targetList.matches('.list')) {
    // save l'emplacement de l'element drop dans le stockage local
    localStorage.setItem(draggedItem.id, targetList.id);

    // add l'element drop à l'elem de liste target
    targetList.append(draggedItem);
  }
}

function restoreDraggedItemLocations() {
  // recuperer tous les elem de liste
  const list_items = document.querySelectorAll('.list-item');

  // Pour chaque element de liste, recuperer son emplacement save dans le stockage local
  for (const list_item of list_items) {
    const location = localStorage.getItem(list_item.id);
    // Si un emplacement a été save pour cet element, ajouter celui ci à l'element de liste correspondant
    if (location) {
      // recuperer l'element de la liste cible
      const targetList = document.getElementById(location);
      // verifier que l'élément cible est bien une liste (et non un element de liste-item)
      if (targetList.classList.contains('list')) {
        targetList.append(list_item);
      }
    }
  }
}

for (let i = 0; i < list_items.length; i++) {
  const item = list_items[i];

  item.addEventListener('dragstart', function () {
    draggedItem = item;
    setTimeout(function () {
      item.style.display = 'none';
    }, 0);
  });

  item.addEventListener('dragend', function () {
    setTimeout(function () {
      draggedItem.style.display = 'block';
      draggedItem = null;
    }, 0);
  });
  }

for (let j = 0; j < lists.length; j++) {
  const list = lists[j];

  list.addEventListener('dragover', function (e) {
    e.preventDefault();
  });

  list.addEventListener('dragenter', function (e) {
    e.preventDefault();
    this.style.backgroundColor = 'rgba(0, 0, 0, 0.2)';
  });

  list.addEventListener('dragleave', function (e) {
    this.style.backgroundColor = 'rgba(0, 0, 0, 0.1)';
  });

  list.addEventListener('drop', saveDraggedItemLocation);
  list.addEventListener('drop', notifyDrop);
}

// Lorsque la page est refresh, restaurer l'emplacement de chaque élément drop et restaurer les notifs
window.addEventListener('load', restoreDraggedItemLocations);
window.addEventListener('load', notifyDrop);

////////////////////
// NOTIFICATIONS  //
////////////////////
function updateProject() {
  // Notif pour la suppression ou l'ajout de tasks et subtasks
  const notification = userName + " a mis à jour son projet le " + new Date().toLocaleDateString('fr-FR');

  // Recupere les notif save dans le local storage sous la forme de string
  let notificationsString = localStorage.getItem('notifications');

  // Si il n'y a pas de notif save, initialise avec un string vide
  if (notificationsString === null) {
    notificationsString = '';
  }

  notificationsString += notification + '\n';

  // save le string dans le local storage
  localStorage.setItem('notifications', notificationsString);

  // recup l'elem de la page HTML où on veut afficher
  const notifications = document.getElementById('notification');

  // màj du content de l'elem avc les notif save
  notifications.innerText = notificationsString;
}
function getListName(targetList) {

  switch(targetList.id) {
    case 'list1':
      return 'TO DO';
    case 'list2':
      return 'In progress';
    case 'list3':
      return 'Done';
      case 'list4':
      return 'In revision';
    default:
      return 'Liste non reconnue';
  }
}

function notifyDrop(e) {
  e.preventDefault();

  const targetList = e.target;
  const listName = getListName(targetList);


  // Créez un nouvel element de notif
  const notification = userName+" a effectué un drag & drop dans le status " + listName + " le " + new Date().toLocaleDateString('fr-FR');


  let notificationsString = localStorage.getItem('notifications');

  if (notificationsString === null) {
    notificationsString = '';
  }

  notificationsString += notification + '\n';

  if(listName == 'TO DO' || listName == 'In progress' || listName == 'Done' || listName == 'In revision'){
    // save le string dans le local storage
    localStorage.setItem('notifications', notificationsString);

    const notifications = document.getElementById('notification');

    // Mettre à jour le contenu de l'élément avec les notifications enregistrées
    notifications.innerText = notificationsString;  }}

window.addEventListener('load', () => {
  // recuperer les notif save dans le local storage en string
  const notificationsString = localStorage.getItem('notifications');


  if (notificationsString !== null) {
    // recup l'elem de la page HTML où on veut afficher
    const notifications = document.getElementById('notification');
    // màj du content de l'elem avc les notif save
    notifications.innerText = notificationsString;
}
});



//////////////////////////////////
// SUPPRIMER DES NOTIFICATIONS  //
//////////////////////////////////
document.getElementById('clear-notifications-button').addEventListener('click', () => {
localStorage.removeItem('notifications');
document.getElementById('notification').innerText = '';
});


