#pragma once
#include <stdexcept>

namespace door {
    
    class Lock {
        public: static const double DEFAULT_DIAMETER;
        public: static const bool DEFAULT_STATE;
        private: double diameter;
        private: bool state;
        private: bool needKey;

        public: Lock(double _diameter = DEFAULT_DIAMETER, bool _state = DEFAULT_STATE);

        public: double getDiameter() const;

        public: void setDiameter(double value);

        public: void setState(bool value);

        public: bool getState() const;

        public: bool getNeedKey() const;


    };
}