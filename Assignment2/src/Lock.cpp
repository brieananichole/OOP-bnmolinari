#include <stdexcept>
#include "Lock.h"

namespace lock
{

const bool Lock::DEFAULT_STATE = false;
const double Lock::DEFAULT_DIAMETER = 2.16;

Lock::Lock(double _diameter, bool _state)
    : diameter(_diameter), state(_state)
    {



}

double Lock::getDiameter() const
{
    return diameter;
}

bool Lock::getState() const
{
    return state;
}

bool Lock::getNeedKey() const
{
    return needKey;
}