function obtenerJSON() {
	// Nombre del archivo JSON
	let nombreArchivo = 'categorias.json';

	// Ruta completa al archivo JSON en el mismo directorio que el archivo JavaScript
	let rutaArchivo = new URL(nombreArchivo, import.meta.url).pathname;

	return new Promise((resolve, reject) => {
		fetch(rutaArchivo)
			.then(response => {
				if (!response.ok) {
					throw new Error('Error al cargar el archivo JSON');
				}
				return response.json();
			})
			.then(data => {
				resolve(data);


			})
			.catch(error => {
				reject(error);
			});
	});
}

function renderNavCat(p) {

	let navElement = document.createElement('div');
	navElement.classList.add('navItems');

	let navLink = document.createElement('a');
	navLink.innerHTML = p;
	navLink.href = catLink(p);

	navElement.appendChild(navLink);

	return navElement;

}

function catLink(p) {

	let str = p.toLowerCase().replace(' ', '-').normalize("NFD").replace(/[\u0300-\u036f]/g, '') + '.html'

	if (str.includes('inicio')) {
		return '../index.html'
	} else {
		return './sitio/' + str
	}

}

async function renderNavbar(container, data) {

	container.appendChild(renderNavCat('Inicio'));

	for (let cat of data) {

		let categoryItem;

		if (cat.constructor === Object) {
			categoryItem = renderNavCat(cat.name);

		} else {
			categoryItem = renderNavCat(cat);
		}

		container.appendChild(categoryItem);

		if (cat.subcategories) {

			let divDropdown = document.createElement('div');
			divDropdown.classList.add('dropdown-content');

			for (let subcat of cat.subcategories) {

				let navSubCat = document.createElement('a');

				if (subcat.constructor === Object) {
					navSubCat.innerHTML = subcat.name;
					navSubCat.href = '';
				} else {
					navSubCat.innerHTML = subcat;
					navSubCat.href = '';
				}
				divDropdown.appendChild(navSubCat);
			}
			categoryItem.appendChild(divDropdown);
		}
	}

	container.appendChild(renderNavCat('Ver todos'));

	return container
}

let navBarContainer = document.getElementById('topnav');

obtenerJSON().then(categories => {

	renderNavbar(navBarContainer, categories.categories)

});