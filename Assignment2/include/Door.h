#pragma once
#include <string>
#include <stdexcept>
#include "Lock.h"
#include "Handle.h"

namespace door {

    class Door {
        public: static const double DEFAULT_HEIGHT;
        public: static const double DEFAULT_WIDTH;
        public: static const std:: string DEFAULT_WOOD;
        private: double width;
        private: double height;
        private: std:: string wood;

    };
}