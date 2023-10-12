#include <cmath>

class Vector {
public:
    double x, y, z;

    double operator&() const {
        return (sqrt(x*x + y*y + z*z));
    }

    Vector operator+(const Vector& other) const {
        Vector result;
        result.x = this->x + other.x;
        result.y = this->y + other.y;
        result.z = this->z + other.z;

        return result;
    }

    Vector operator-(const Vector& other) const {
        Vector result;
        result.x = this->x - other.x;
        result.y = this->y - other.y;
        result.z = this->z - other.z;

        return result;
    }

    double operator%(const Vector& other) const {
        double result;
        result = this->x * other.x;
        result += this->y * other.y;
        result += this->z * other.z;

        return result;
    }

    Vector operator*(const Vector& other) const {
        Vector result;
        result.x = this->y*other.z - this->z*other.y;
        result.y = -(this->x*other.z - this->z*other.x);
        result.z = this->x*other.y - this->y*other.x;

        return result;
    }

    Vector operator+(const float d) const {
        Vector result;
        result.x = this->x + d;
        result.y = this->y + d;
        result.z = this->z + d;

        return result;
    }

    Vector operator-(const float d) const {
        Vector result;
        result.x = this->x - d;
        result.y = this->y - d;
        result.z = this->z - d;

        return result;
    }

    Vector operator/(const float d) const {
        Vector result;
        result.x = this->x / d;
        result.y = this->y / d;
        result.z = this->z / d;

        return result;
    }

    Vector operator*(const float d) const {
        Vector result;
        result.x = this->x * d;
        result.y = this->y * d;
        result.z = this->z * d;

        return result;
    }
};