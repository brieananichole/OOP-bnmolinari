#pragma once
#include <stdexcept>

namespace lock {
    
    class Lock {
        public: static const double DEFAULT_DIAMETER;
        public: static const bool DEFAULT_STATE;
        public: const double diameter;
        private: bool state;
        private: bool needKey;
        public: Lock(double _diameter = DEFAULT_DIAMETER, bool _state = DEFAULT_STATE);

        public: double getDiameter() const;

        public: void setState(bool value);

        public: bool getState() const;

        public: bool setNeedKey(bool value);

        public: bool getNeedKey() const;


    };
}