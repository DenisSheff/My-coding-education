package org.example.seminar2.cw2;

public class Vector {
    private double x;
    private double y;
    private double z;

    public Vector() {
    }

    public Vector(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }

    public double getZ() {
        return z;
    }

    public void setZ(double z) {
        this.z = z;
    }

    @Override
    public String toString() {
        return "Vector{" +
                "x=" + x +
                ", y=" + y +
                ", z=" + z +
                '}';
    }

//    return vector length
    public double length() {
        return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2) + Math.pow(z, 2));
    }

    public double scalarProduct(Vector vector) {
        return x * vector.x + y * vector.y + z * vector.z;
    }

    public Vector vectorProduct(Vector vector) {
        return new Vector(y * vector.z - z * vector.y,
                          z * vector.x - x * vector.z,
                          x * vector.y - y * vector.x);
    }

    public double cos(Vector vector) {
        return scalarProduct(vector) / (vector.length() * length());
    }

    public Vector vectorSum(Vector vector) {
        return new Vector(x + vector.x, y + vector.y, z + vector.z);
    }

    public Vector vectorDifference(Vector vector) {
        return new Vector(x - vector.x, y - vector.y, z - vector.z);
    }
}
