// Find the total area covered by two rectilinear rectangles in a 2D plane.
// Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
//      square1, two diagonal coordinates: (A,B) and (C,D)
//      square2, two diagonal coordinates: (E,F) and (G,H)
//
// Assume that the total area is never beyond the maximum possible value of int.

/**
 * @param {number} A
 * @param {number} B
 * @param {number} C
 * @param {number} D
 * @param {number} E
 * @param {number} F
 * @param {number} G
 * @param {number} H
 * @return {number}
 */

var computeArea = function (A, B, C, D, E, F, G, H) {
    // Total area = two square areas - overlapped square area(if exists)

    var sqArea1 = Math.abs((C - A) * (D - B))
    var sqArea2 = Math.abs((G - E) * (H - F))

    // find overlapped area square's left X coordinate
    var leftX = Math.max(A, E)
    // find overlapped area square's right X coordinate
    var rightX = Math.max(Math.min(C, G), leftX)

    // find overlapped area square's bottom Y coordinate
    var bottomY = Math.max(B, F)
    // find overlapped area square's top Y coordinate
    var topY = Math.max(Math.min(D,H), bottomY)

    var overlappedArea = (rightX - leftX) * (topY - bottomY)

    return sqArea1 + sqArea2 - overlappedArea

};