async function httpClient(url) {
    let response = await fetch(url);
    let result = await response.json();
    return result
}

function createProductCard(p) {
    // se crea un elemento div
    let productCard = document.createElement("div");
    // se agrega clase al div
    productCard.classList.add('prod-card');

    // title
    let productTitle = document.createElement("h3");
    productTitle.classList.add('prod-card-title');
    // se agrega el titulo del producto al title
    productTitle.innerHTML = p.name;

    // precio
    let productPrice = document.createElement("p");
    productPrice.classList.add('prod-card-price');
    productPrice.innerHTML = `\$ ${p.basePrice}`;

    // boton ver mas
    let productVermas = document.createElement('button');
    productVermas.classList.add('prod-vermas');
    productVermas.innerHTML = 'Ver más';
    productVermas.setAttribute('type', 'button')

    // imagen
    let productImg = document.createElement('img');
    productImg.classList.add('prod-img');
    productImg.src = p.thumbnailImage;

    // se agregan elementos a la card
    productCard.appendChild(productImg);
    productCard.appendChild(productTitle);
    productCard.appendChild(productPrice);
    productCard.appendChild(productVermas);

    return productCard;
}

async function addElement(){
    // traigo objeto con productos
    let result = await httpClient('https://dummyapi.online/api/products')

    // guardo id del container
    let productGrid = document.getElementById('prod-grid');

    // itero sobre objeto
    for (let p of result) {

        // por cada producto se crea una card
        let productCard = createProductCard(p);

        // se agrega card al prod-grid
        productGrid.appendChild(productCard);
    }
}

addElement()
