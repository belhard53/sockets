# HTTP, sockets and start Flask

HTTP - Hyper Text Transport Protocol
Протокол передачи гипер текста
Основной порт HTTP - 80
Основной порт HTTPS - 443
HTTP/HTTPS могут использовать различные протоколы передачи данных, основные из них
это TCP/UDP
TCP - Transmission Control Protocol
Данный протокол медленнее чем UDP, но обладает преимуществом, так как гарантирует
доставку пакетов, его принцип работы прост:
1. Перед отправкой он проверяет готов ли клиент получать информацию
2. Отправляет пакет
3. Получает подтверждение о получении пакета, если пакет не получен, то он повторяет
его отправку до получения подтверждения или разрыва соединения
UDP - User Datagram Protocol
Данный протокол не гарантирует доставки пакетов, так как оне не проверяет готовность
клиента и не запрашивает подтверждения, а так же может слать пакеты в случайном
порядке, в результате чего есть высокий процент потери пакетов, но за счет этого он
значительно быстрее
! Не стоит думать, что TCP не обладает потерями, на самом деле даже у данного протокола
они встречаются, редко и не в значительном количестве.
Структура HTTP
1. Стартовая строка (start line) — используется для описания версии используемого
протокола и другой информации — вроде запрашиваемого ресурса или кода ответа.
Как можно понять из названия, ее содержимое занимает ровно одну строчку.
2. HTTP-заголовки (HTTP Headers) — несколько строчек текста в определенном
формате, которые либо уточняют запрос, либо описывают содержимое тела
сообщения.
3. Пустая строка, которая сообщает, что все метаданные для конкретного запроса или
ответа были отправлены.
4. Опциональное тело сообщения, которое содержит данные, связанные с запросом, либо
документ (например HTML-страницу), передаваемый в ответе.
Методы HTTP запросов:

GET - Позволяет запросить данные с сервера, не обладает телом, данные можно передать либо
через Headers либо через сам запрос в ссылке используя Path и Query параметры
Пример Path параметра:
https://some-site.com/category/1
Category - Path параметр указывающий на то, что мы запрашиваем информацию о категориях
1 - указывает на то, что мы запрашиваем информацию о конкретной категории
Пример Query параметра:
https://some-site.com/laptop?manufactory=lenovo&ram[from]=8
Manufactory и ram[from] в данном случае это Query параметры, а Lenovo и 8 их значения

POST - Используется для отправки данных на сервер, как правило для создания нового
ресурса (например публикация нового поста), обладает телом, передать можно
практически что угодно

HEAD - Аналогичен GET, но ответ от сервера не содержит тело, только заголовки,
используется чаще всего для того, чтобы узнать техническую информацию по ответу,
который был бы получен при GET, например размер тела

PUT - Аналогичен POST, но так же может быть использован для обновления существующего
ресурса, в таком случае тело запроса должно нести как обновленные данные, так и
данные которые не были изменены

PATH - Служит для частичного обновления существующего ресурса

DELETE - Используется для удаления существующего ресурса

OPTIONS - Позволяет получить информацию о сервере и допустимых HTTP запросов, может
использоваться в связке с методами POST/PUT/PATCH/DELETE для получения
разрешения на осуществления данных запросов

Структура URL:
http:// https:// ws:// wss:// и тд. - схема запроса
some-site.com - хост
:80 :443 - порт, если не указывать порт, то будет использоваться стандартный порт схемы
запроса

Осуществление запросов с использованием Python
Для осуществления запросов существует ряд различных библиотек: requests, httpx, aiohttp и тд
Мы рассмотрим 2 основных и самых популярных - requests/aiohttp
Все библиотеки имеют примерно одинаковый интерфейс, но со своими особенностями
В любом случае рекомендуется всегда использоваться сессии, если они предоставляются
библиотекой которую вы используется

У Каждой сессии есть методы соответствующие методу запроса и ряд основных
Аргументов:

Url - ссылка (url) запроса, несет в себе все до Query параметров
Params - аргумент для передачи Query параметров в виде словаря тем самым позволяет
избавиться от необходимости приходить их нужному виду согласно стандарту

Data - тело запроса, чаще всего используется для передачи текстовой информации, например
HTML или данных из формы

Json - тело запроса для передачи json файла, передается в качестве словаря, что избавляет нас
от необходимости самостоятельно его сериализовать

File - тело запроса для передачи файла (картинка, документ и тд)
Headers - заголовки запроса, передается в качестве словаря

Cookies - куки запроса, как правило Передается в качестве словаря, но стоит обратить
внимание, что в некоторых библиотеках это запрещено и существует собственные
типы данных для передачи cookies

Данные аргументы вы найдете в 100% используемых библиотек
Ответ от сервера по своей структуре аналогичен запросу, дополнительно несет статус код
Статус кода HTTP:
100+ - информационные, редкоиспользуьемые, чаще всего можно встретить при работе с
WebSocket
200+ - успешные статусы
300+ - статусы перенаправления
400+ - ошибка на стороне пользователя
500+ - ошибка на стороне сервера
Полный перечень с описанием можно посмотреть здесь
https://developer.mozilla.org/ru/docs/Web/HTTP/Status

AioHttp, в отличии от Requests, является асинхронной библиотекой, что накладывает
необходимость в использовании async/await синтаксиса, но не следует писать await
перед каждым методом ClientSession и других асинхронных библиотек, чтобы точно
узнать, является ли метод/функция асинхронной и ее следует «эвейтить» вы всегда
можете навестить на нее (если используете Pycharm) и посмотреть ее документацию
! Если функция/метод объявлены как async def/перед ней написано awaitable/возвращаемый
тип данных Сoroutine - до данная функци/метод является асинхронной
Так же aiohttp имеет встроенную возможность работать с WebSocket
! Обратите внимание, что данная библиотека имеет как клиентскую часть так и серверную,

что позволяет при необходимости написать полноценный веб ресурс или API
Полезные ссылки:
https://requests.readthedocs.io/en/latest/
https://docs.aiohttp.org/en/stable/
