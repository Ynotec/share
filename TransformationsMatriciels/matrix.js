export default class Matrix {
    // Applique une matrice de transformation à un point
    static transformPoint(point, matrix) {
        const x = point.x * matrix[0][0] + point.y * matrix[0][1] + matrix[0][2]
        const y = point.x * matrix[1][0] + point.y * matrix[1][1] + matrix[1][2]
        return { x, y }
    }

    // Matrice de rotation de 270 degrés
    static rotation270() {
        return [
            [0, 1, 0],
            [-1, 0, 0],
            [0, 0, 1]
        ]
    }
    
    // Matrice de rotation de 180 degrés
    static rotation180() {
        return [
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ]
    }

    // Matrice de rotation de 90 degrés
    static rotation90() {
        return [
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ]
    }

    // Matrice de translation
    static translation(dx, dy) {
        return [
            [1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]
        ]
    }

    // Matrice de mise à l'échelle
    static scaling(k) {
        return [
            [k, 0, 0], 
            [0, k, 0], 
            [0, 0, 1]
        ]
    }
}