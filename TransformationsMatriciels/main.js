import Renderer from './renderer.js'
import UIManager from './uimanager.js'
import Matrix from './matrix.js'

const renderer = new Renderer(document.getElementById('canvas')) // passe le canevas au renderer
const uiManager = new UIManager() // gère l'interface utilisateur

// Fonction pour dessiner la scène
function draw() {
    renderer.clear()
    renderer.drawGrid()
    const polygon = uiManager.getPolygonFromInputs()
    const color = uiManager.getColor()
    renderer.drawShape(polygon, color)
}

// écouteurs d'évènements pour le nombre de points
uiManager.pointCountInput.addEventListener('input', () => {
    uiManager.generatePointInputs(uiManager.getPointCount())
    draw()
})

// écouteurs d'évènements pour les changements de points 1, 2, ... n
uiManager.pointsContainer.addEventListener('input', () => {
    draw()
})

// écouteur d'évènement pour le changement de couleur
uiManager.colorPicker.addEventListener('input', () => {
    draw()
})

// Boutons de rotation récupération des éléments
const rotateButton90 = document.getElementById('rotate90')
const rotateButton180 = document.getElementById('rotate180')
const rotateButton270 = document.getElementById('rotate270')

// Ajout des écouteurs d'évènements pour les boutons de rotation
rotateButton90.addEventListener('click', () => {
    const currentPoints = uiManager.getPolygonFromInputs()
    const matrix = Matrix.rotation90()
    const newPoints = currentPoints.map(point => {
        return Matrix.transformPoint(point, matrix)
    })
    uiManager.updateInputs(newPoints)
    draw()
})

rotateButton180.addEventListener('click', () => {
    const currentPoints = uiManager.getPolygonFromInputs()
    const matrix = Matrix.rotation180()
    const newPoints = currentPoints.map(point => {
        return Matrix.transformPoint(point, matrix)
    })
    uiManager.updateInputs(newPoints)
    draw()
})

rotateButton270.addEventListener('click', () => {
    const currentPoints = uiManager.getPolygonFromInputs()
    const matrix = Matrix.rotation270()
    const newPoints = currentPoints.map(point => {
        return Matrix.transformPoint(point, matrix)
    })
    uiManager.updateInputs(newPoints)
    draw()
})

// Écouteur d'évènement pour le bouton de translation
document.getElementById('btnTranslate').addEventListener('click', () => {
    const currentPoints = uiManager.getPolygonFromInputs()

    // récupérer les valeurs de translation depuis les champs input
    const dx = parseFloat(document.getElementById('transX').value)
    const dy = parseFloat(document.getElementById('transY').value)

    // Obtenir la matrice de translation
    const matrix = Matrix.translation(dx, dy)

    // Appliquer la transformation et mettre à jour les inputs et dessiner la forme
    const newPoints = currentPoints.map(p => Matrix.transformPoint(p, matrix))
    uiManager.updateInputs(newPoints)
    draw()
});

// Écouteur d'évènement pour le bouton de mise à l'échelle
document.getElementById('btnScale').addEventListener('click', () => {
    const currentPoints = uiManager.getPolygonFromInputs()
    const scaleFactor = parseFloat(document.getElementById('scaleFactor').value)
    const matrix = Matrix.scaling(scaleFactor) // Obtenir la matrice de mise à l'échelle

    // Appliquer la transformation et mettre à jour les inputs et dessiner la forme
    const newPoints = currentPoints.map(p => Matrix.transformPoint(p, matrix))
    uiManager.updateInputs(newPoints)
    draw()
})

// Boutons de formes prédéfinies
document.getElementById('square').addEventListener('click', () => {
    const square = uiManager.getPredefinedShape('square')
    uiManager.pointCountInput.value = square.length
    uiManager.generatePointInputs(square.length)
    uiManager.updateInputs(square)
    draw()
})

document.getElementById('triangle').addEventListener('click', () => {
    const triangle = uiManager.getPredefinedShape('triangle')
    uiManager.pointCountInput.value = triangle.length
    uiManager.generatePointInputs(triangle.length)
    uiManager.updateInputs(triangle)
    draw()
})

document.getElementById('quadri').addEventListener('click', () => {
    const quadri = uiManager.getPredefinedShape('quadri')
    uiManager.pointCountInput.value = quadri.length
    uiManager.generatePointInputs(quadri.length)
    uiManager.updateInputs(quadri)
    draw()
})

// Initialisation au démarrage
// Générer les inputs par défaut et lancer draw()
uiManager.generatePointInputs(uiManager.getPointCount())
draw()