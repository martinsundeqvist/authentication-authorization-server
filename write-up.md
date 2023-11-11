# OpenID / Oauth 2.0 implementation

This write-up outlines a first principles appraoch to building the authentication and authorization servers implementing the OpenID and OAuth 2.0 protocols. The idea is to avoid the use of external libraries and focusing on a barebones implementation that implements a core flow.

I will say up front I'm not expert on this protocols, and that I'm part doing this write-up to cement a better understanding of these protocols and how the sometimes opaque frameworks implmenting them work.

## The basics
In our first iteration, what we need is the following set of entities:
- Resource owner: The resource owner is the owner of a resource (some data), i.e. "us" in this case
- Resource server: The resource server is the entity hosting the protected resource
- Client: The client is some entity that would like to gain access
- Authorization server: The authorization server is a server that enables us to complete the authorization flow as described by the Oauth 2.0 protocol.
- Authentication server: The authentication server is a server that enables us to carry out authentication as described in OpenID connect protocol.

## The problem
In our scenario, we are going to imagine that the year is 2000 and the masterpiece https://en.wikipedia.org/wiki/Tony_Hawk%27s_Pro_Skater_2. Your parents can't quite afford the full game, but you and your friends are grinding the demo you got in cereal box like there's no tomorrow.

Through diligent study, you've distilled this set of special moves:


```
           6.1) Special Moves
-=--=--=--=--=--=--=--=--=--=--=--=--=-

Left, Right, Square - Nollie Underflip
Left, Right, Circle - Pogo Air
Right, Left, Circle - Christ Air
Left, Right, Triangle - Heelflip Darkslide
Right, Left, Triangle - Layback Grind
```

that you currently in a text file **secret-dope-moves.txt** on your server. Your don't hoard all your moves however, there is another file **public-dope-moves.txt**

```
-=--=--=--=--=--=--=--=--=--=--=--=--=-
            6.2) Grab Moves
-=--=--=--=--=--=--=--=--=--=--=--=--=-

Up, Circle - Airwalk
Up/Right, Circle - Rocket Air
Right, Circle - Indy
Right/Down, Circle - Madonna
Down, Circle - Indy Stiffy
Down/Left, Circle - Benihana
Left, Circle - Crossbone
Up/Left, Circle - Judo
```

that other users on the server are allowed to read (but not update).

## In our example
In our example, we are the **resource owner** of the skate-combo text files. The server hosting our skateboarding website is the **resource server**. The **client** would be the web browser used either by ourselves or someone else to access one of the files.

Here we recognize there is a need for two different things:
1. Clients need to be able to authenticate themselves, i.e. show "who" they are
2. Clients need to be able to demonstrate to the resource server they are allowed certain access

The authorization problem will be handled by an authorization server. The authentication problem will be handled by an authentication server.