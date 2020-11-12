

###
#
# This exception is raised when something failed to use mode.
#
###
class ModuleNotUseException(Exception):
  def __str__(self):
    return "Please use a module"
###
#
# Mixin that should be included in all exceptions that can be raised from the
# framework so that they can be universally caught.  Framework exceptions
# automatically extended Rex exceptions
#
###


###
#
# This exception is raised when one or more options failed
# to pass data store validation.  The list of option names
# can be obtained through the options attribute.
#
###

class OptionValidateError(Exception):
    def __str__(self):
        return "The following options failed to validate:"


###
#
# This exception is raised when something failed to validate properly.
#
###
class ValidationError(Exception):
    def __str__(self):
        return "One or more requirements could not be validated."


###
#
# This exception is raised when the module cache is invalidated.  It is
# handled internally by the ModuleManager.
#
###

class ModuleCacheInvalidated(Exception):
    def __str__(self):
        return "ModuleCacheInvalidated"


##
#
# Encoding exceptions
#
##

###
#
# This exception is raised to indicate that an encoding error of some sort has
# occurred.
#
###
class EncodingError(Exception):
    def __str__(self):
        return "An encoding exception occurred."


###
#
# Thrown when an encoder fails to find a viable encoding key.
#
###
class NoKeyError(Exception):
    def __str__(self):
        return "A valid encoding key could not be found."


###
#
# Thrown when an encoder fails to encode a buffer due to a bad character.
#
###
"""
class BadcharError < EncodingError
  def initialize(buf = nil, index = nil, stub_size = nil, char = nil)
    @buf       = buf
    @index     = index
    @stub_size = stub_size
    @char      = char
  end

  def to_s
    # Deal with elements of a String being an instance of String instead of
    # Integer in ruby 1.9.
    if (char.respond_to? :ord)
      c = char.ord
    else
      c = char
    end
    if (c)
      return "Encoding failed due to a bad character (index=#{index}, char=#{sprintf("0x%.2x", c)})"
    else
      return "Encoding failed due to a nil character"
    end
  end

  attr_reader :buf, :index, :stub_size, :char
end
"""


###
#
# This exception is raised when no encoders succeed to encode a buffer.
#
###
class NoEncodersSucceededError(Exception):
    def __str__(self):
        return "No encoders encoded the buffer successfully."


###
#
# Thrown when an encoder fails to generate a valid opcode sequence.
#
###
class BadGenerateError(Exception):
    def __str__(self):
        return "A valid opcode permutation could not be found."


##
#
# Exploit exceptions
#
##

###
#
# This exception is raised to indicate a general exploitation error.
#
###
class ExploitError(Exception):
    def __str__(self):
        return "An exploitation error occurred."


###
#
# This exception is raised to indicate a general auxiliary error.
#
###
class AuxiliaryError(Exception):
    def __str__(self):
        return "An auxiliary error occurred."


###
#
# This exception is raised if a target was not specified when attempting to
# exploit something.
#
###
class MissingTargetError(Exception):
    def __str__(self):
        return "A target has not been selected."


###
#
# This exception is raised if a payload was not specified when attempting to
# exploit something.
#
###
class MissingPayloadError(Exception):
    def __str__(self):
        return "A payload has not been selected."


###
#
# This exception is raised if a valid action was not specified when attempting to
# run an auxiliary module.
#
###
class MissingActionError(Exception):
    #:todo
    def __str__(self):
        return "Invalid action: #{@reason}"


###
#
# This exception is raised if an incompatible payload was specified when
# attempting to exploit something.
#
###
class IncompatiblePayloadError(Exception):
    def __str__(self):
        #:todo
        return "#{pname} is not a compatible payload."


#
# The name of the payload that was used.
#
# attr_reader :pname


class NoCompatiblePayloadError(Exception):
    def __str__(self):
        #:todo
        return 'NoCompatiblePayloadError'


##
#
# NOP exceptions
#
##

###
#
# This exception is raised to indicate that a general NOP error occurred.
#
###
class NopError(Exception):
    def __str__(self):
        #:todo
        return "A NOP generator error occurred."


###
#
# This exception is raised when no NOP generators succeed at generating a
# sled.
#
###
class NoNopsSucceededError(Exception):
    def __str__(self):
        #:todo
        return "No NOP generators succeeded."


##
#
# Plugin exceptions
#
##

class PluginLoadError(Exception):
    def __str__(self):
        #:todo
        return "This plugin failed to load: #{reason}"


##
#
# This exception is raised if a payload option string exceeds the maximum
# allowed size during the payload generation.
#
##
class PayloadItemSizeError(Exception):
    def __str__(self):
        #:todo
        return "Option value: #{item.slice(0..30)} is too big (Current length: #{item.length}, Maximum length: #{max_size})."

# attr_reader :item # The content of the payload option (for example a URL)
# attr_reader :max_size # The maximum allowed size of the payload option
