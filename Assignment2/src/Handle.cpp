#include <stdexcept>
#include "Handle.h"

namespace handle
{

const bool Lock::DEFAULT_STATE = false;
const double Lock::DEFAULT_DIAMETER = 2.16;

Lock::Lock(double _diameter, bool _state)
    : diameter(_diameter), state(_state)



}