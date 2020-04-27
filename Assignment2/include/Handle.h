#pragma once
#include <string>
#include <stdexcept>

namespace door {

    class Handle {
        public: static const double DEFAULT_DIAMETER;
        public: static const std:: string DEFAULT_FINISH;
        public: static const std:: string DEFAULT_MATERIAL;
        private: double diameter;
        private: bool finish;
        private: std:: string material;

        public: Handle(double _diameter = DEFAULT_DIAMETER, std::string _finish = DEFAULT_FINISH, std:: string _material= DEFAULT_MATERIAL);

        public: double getDiameter() const;

        public: void setDiameter(double value);

        public: std:: string getMaterial() const;

        public: void setMaterial(std:: string value);

        public: std:: string getFinish() const;

        public: void setFinish(std:: string value);

    };

}