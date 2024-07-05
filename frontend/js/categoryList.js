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

function renderCategoryItem(p) {
	// se crea un elemento div
	let categoryElement = document.createElement("div");
	// se agrega clase al div
	categoryElement.classList.add('cat-marcas-container');

	let categoryHeader = document.createElement("h3");
	categoryHeader.classList.add('headers-columnas');

	let categoryHeaderLink = document.createElement('a');
	categoryHeaderLink.classList.add('cat-header-link');
	categoryHeaderLink.innerHTML = p;
	categoryHeaderLink.href = '';

	categoryHeader.appendChild(categoryHeaderLink);
	categoryElement.appendChild(categoryHeader);

	return categoryElement;
}

function renderSubcategoryItem(p) {

	let subCatElement = document.createElement('ul');
	subCatElement.classList.add('cat-marcas-lista');

	let subCatListItem = document.createElement('li');
	subCatListItem.classList.add('lista-marcas-li');

	let subCatListLink = document.createElement('a');
	subCatListLink.classList.add('cat-links');
	subCatListLink.innerHTML = p;
	subCatListLink.href = '';

	subCatListItem.appendChild(subCatListLink);
	subCatElement.appendChild(subCatListItem);

	return subCatElement;
}

async function renderCategoriesList(container, data) {

	for (let cat of data) {

		let categoryItem;
		let subCategoryItem;

		if (cat.constructor === Object) {
			categoryItem = renderCategoryItem(cat.name);

		} else {
			categoryItem = renderCategoryItem(cat);

		}
		container.appendChild(categoryItem);

		if (cat.subcategories) {

			for (let subcat of cat.subcategories) {
				if (subcat.constructor === Object){
					subCategoryItem = renderSubcategoryItem(subcat.name)
				}else{
					subCategoryItem = renderSubcategoryItem(subcat)
				}
				container.appendChild(subCategoryItem);
			}
		}
	}

	return container

}

let productGrid = document.getElementById('prod-categorias');

obtenerJSON().then(categories => {

	renderCategoriesList(productGrid, categories.categories);

});
