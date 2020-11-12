class API:
      # @note This is a like.  The API version is not semantically version and it's version has actually never changed
      #    even though API changes have occured.  DO NOT base compatibility on this version.
      Version={
        'MAJOR':'1',
        'MINOR':'0',
        'PATCH' :'0'
      }
      for k,v in Version.items():
          if k == "MAJOR":
            print("version of thg => {}".format(k))

