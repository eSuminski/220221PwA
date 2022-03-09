from unittest.mock import Mock

from psycopg import OperationalError

m = Mock(side_effect=OperationalError("Could not connect to database"))

m()
