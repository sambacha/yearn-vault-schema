# Development Documents

> Reference Regex for usage in the schema file

```pearl
/
# protocol user host-ip port path path path querystring fragment
^
#protocol
(?:(?<scheme>[a-zA-Z][a-zA-Z\d+-.]*):)?
(?:
  (?:
    (?:
        \/\/
        (?:
            #userinfo
            (?:((?:[a-zA-Z\d\-._~\!$&'()*+,;=%]*)(?::(?:[a-zA-Z\d\-._~\!$&'()*+,;=:%]*))?)@)?
            #host-ip
            ((?:[a-zA-Z\d-.%]+)|(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|(?:\[(?:[a-fA-F\d.:]+)\]))?
            #port
            (?::(\d*))?
        )
    )
    #slash-path
    (
        (?:\/[a-zA-Z\d\-._~\!$&'()*+,;=:@%]*)*
    )
  )
 #slash-path
 |(\/(?:(?:[a-zA-Z\d\-._~\!$&'()*+,;=:@%]+(?:\/[a-zA-Z\d\-._~\!$&'()*+,;=:@%]*)*))?)
 #path
 |([a-zA-Z\d\-._~\!$&'()*+,;=:@%]+(?:\/[a-zA-Z\d\-._~\!$&'()*+,;=:@%]*)*)
)?
#querystring
(?:\?([a-zA-Z\d\-._~\!$&'()*+,;=:@%\/?]*))?
#fragment
(?:\#([a-zA-Z\d\-._~\!$&'()*+,;=:@%\/?]*))?
$
/x
```
