-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Discrição da investigação
SELECT description FROM crime_scene_reports
WHERE day = 28 AND month = 7 AND year = 2020 AND street ="Chamberlin Street";

-- Relatório das testemunhas
SELECT id, name, transcript FROM interviews
WHERE day = 28 AND year = 2020 AND month = 7
AND id IN (161, 162, 163);

-- Relatório das cameras de segurança
SELECT license_plate FROM courthouse_security_logs
WHERE day = 28 AND month = 7 AND year = 2020
AND hour = 10 AND minute > 15 AND minute <26 and activity = "exit";

-- Relatório de saques no banco na Fifer Street
SELECT account_number FROM atm_transactions
WHERE day = 28 AND month = 7 AND year = 2020
AND atm_location = "Fifer Street" AND transaction_type = "withdraw";

-- Relatório de telefonemas
SELECT caller FROM phone_calls
WHERE day = 28 AND month = 7 AND year = 2020
AND duration <61;

-- Horário do voô mais cedo no dia seguinte saindo de fiftyville
SELECT id, destination_airport_id, hour, minute FROM flights
WHERE origin_airport_id = 8 AND day = 29 AND month = 7 AND year = 2020
ORDER BY hour, minute LIMIT 1;

-- Destino do voô acima
SELECT full_name, city FROM airports
WHERE id = 4;

-- Procurando um possível assaltante com base nos dados das testemunhas
SELECT people.name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
WHERE bank_accounts.account_number in (
    SELECT account_number FROM atm_transactions
    WHERE day = 28 AND month = 7 AND year = 2020
    AND atm_location = "Fifer Street" AND transaction_type = "withdraw"
) AND people.phone_number IN (
    SELECT caller FROM phone_calls
    WHERE day = 28 AND month = 7 AND year = 2020
    AND duration <61
) AND license_plate IN (
   SELECT license_plate FROM courthouse_security_logs
    WHERE day = 28 AND month = 7 AND year = 2020
    AND hour = 10 AND minute > 15 AND minute <26 and activity = "exit"
) AND passport_number IN (
    SELECT passengers.passport_number from flights
    JOIN passengers ON passengers.flight_id = flights.id
    WHERE flights.id = 36
);

-- Encontrando o cumplice --

-- Procurando para quem Ernest ligou
SELECT receiver FROM phone_calls
WHERE caller = (
    SELECT phone_number FROM people
    WHERE name = "Ernest"
) AND day = 28 AND month = 7 AND year = 2020
AND duration < 61;

-- Procurando a pessoa do número acima
SELECT name FROM people
WHERE phone_number = (
    SELECT receiver FROM phone_calls
    WHERE caller = (
        SELECT phone_number FROM people
        WHERE name = "Ernest"
    ) AND day = 28 AND month = 7 AND year = 2020
    AND duration < 61
);