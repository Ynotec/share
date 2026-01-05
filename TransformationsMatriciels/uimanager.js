export default class UIManager {
    constructor() {
        // récupère les éléments HTML nécessaires
        this.pointCountInput = document.getElementById('pointCount')
        this.pointsContainer = document.querySelector('.points')
        this.colorPicker = document.getElementById('colorPicker')
    }

    // retourne le nombre de points défini par l'utilisateur
    getPointCount() {
        return parseInt(this.pointCountInput.value)
    }

    // retourne la couleur choisie par l'utilisateur
    getColor() {
        return this.colorPicker.value
    }

    // Génère dynamiquement les champs d'entrée pour les points
    generatePointInputs(count) {
        this.pointsContainer.innerHTML = '' // vide le conteneur avant de le remplir
        for (let i = 0; i < count; i++) {
            const pointDiv = document.createElement('div')
            pointDiv.classList.add('point-input')
            pointDiv.innerHTML = `
                <div class="point">
                    <label>Point ${i + 1}:</label>
                    <input type="number" class="x-coordinate-${i}" placeholder="X" value="0">
                    <input type="number" class="y-coordinate-${i}" placeholder="Y" value="0">
                </div>
            `
            this.pointsContainer.appendChild(pointDiv)
        }
    }

    // Récupère les coordonnées des points depuis les champs d'entrée
    getPolygonFromInputs() {
        const numberOfSides = this.getPointCount()
        const newPolygon = []
        for (let i = 0; i < numberOfSides; i++) {
            const xInput = document.querySelector(`.x-coordinate-${i}`)
            const yInput = document.querySelector(`.y-coordinate-${i}`)
            const x = parseFloat(xInput.value)
            const y = parseFloat(yInput.value)
            newPolygon.push({x, y})
        }
        return newPolygon
    }

    // Met à jour les champs HTML avec les nouvelles coordonnées
    updateInputs(polygon) {
        polygon.forEach((point, index) => {
            const xInput = document.querySelector(`.x-coordinate-${index}`);
            const yInput = document.querySelector(`.y-coordinate-${index}`);
            
            // On limite à 3 décimales pour éviter les nombres à rallonge
            if(xInput) xInput.value = point.x.toFixed(0);
            if(yInput) yInput.value = point.y.toFixed(0);
        });
    }

    // Retourne une forme prédéfinie en fonction du nom donné
    getPredefinedShape(shapeName) {
        const shapes = {
            triangle: [
                {x: 0, y: 50},
                {x: -43.3, y: -25},
                {x: 43.3, y: -25}
            ],
            quadri: [
                {x: -60, y: 30},
                {x: 60, y: 30},
                {x: 60, y: -30},
                {x: -60, y: -30}
            ],
            square: [
                {x: -30, y: 30},
                {x: 30, y: 30},
                {x: 30, y: -30},
                {x: -30, y: -30}
            ],
        }
        return shapes[shapeName] || []
    }
}