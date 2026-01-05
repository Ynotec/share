export default class Renderer {
    constructor(canvas) {
        // initialise le contexte de rendu
        this.canvas = canvas
        this.ctx = canvas.getContext('2d')
        this.width = canvas.width
        this.height = canvas.height
        
        // centre du canevas
        this.centerX = this.width / 2
        this.centerY = this.height / 2
    }

    // Convertit les coordonnées mathématiques en coordonnées écran
    toScreenX(xMath) {
        return this.centerX + xMath
    }

    // Convertit les coordonnées mathématiques en coordonnées écran
    toScreenY(yMath) {
        return this.centerY - yMath
    }

    // Dessine une grille de référence
    drawGrid() {
        this.ctx.clearRect(0, 0, this.width, this.height)
        this.ctx.beginPath()
        this.ctx.strokeStyle = '#ccc'
        this.ctx.lineWidth = 1

        // Axe X
        this.ctx.moveTo(0, this.centerY)
        this.ctx.lineTo(this.width, this.centerY)
        
        // Axe Y
        this.ctx.moveTo(this.centerX, 0)
        this.ctx.lineTo(this.centerX, this.height)

        this.ctx.stroke()

        // Labels
        this.ctx.fillStyle = 'black'
        this.ctx.fillText("X", this.width - 20, this.centerY - 10)
        this.ctx.fillText("Y", this.centerX + 10, 20)
    }

    // Dessine une forme donnée avec une couleur spécifique
    drawShape(shape, color) {
        this.ctx.beginPath()
        this.ctx.strokeStyle = color // utilise la couleur spécifiée
        this.ctx.lineWidth = 2 // épaisseur de ligne plus visible

        // Parcourt les points de la forme et les dessine
        shape.forEach((point, index) => {
            const screenX = this.toScreenX(point.x)
            const screenY = this.toScreenY(point.y)
            if (index === 0) {
                this.ctx.moveTo(screenX, screenY)
            } else {
                this.ctx.lineTo(screenX, screenY)
            }
        })
        this.ctx.closePath()
        this.ctx.stroke()
    }

    // Efface le canevas
    clear() {
        this.ctx.clearRect(0, 0, this.width, this.height)
    }
}