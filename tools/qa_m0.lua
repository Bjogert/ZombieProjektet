-- Optional read-only runtime checks for the synthetic M0 house.
-- Copy to the installed test mod's 42/media/lua/client/ only for QA.
-- It is deliberately outside the distributable mod source.
local function report(label, actual, expected)
    local status = actual == expected and "PASS" or "FAIL"
    print("[ZombieProjektet QA] " .. status .. " " .. label
        .. " actual=" .. tostring(actual) .. " expected=" .. tostring(expected))
end

local function runChecks()
    local player = getSpecificPlayer(0)
    local cell = getCell()
    if not player or not cell or player:getX() < 110 or player:getX() > 140
            or player:getY() < 110 or player:getY() > 140 then
        print("[ZombieProjektet QA] SKIP: player is outside the synthetic test area")
        return
    end
    local edges = {
        {"west wall", 120, 126, -1, 0, true},
        {"north wall", 122, 120, 0, -1, true},
        {"east wall", 129, 126, 1, 0, true},
        {"south wall", 125, 127, 0, 1, true},
        {"clear interior", 125, 124, 1, 0, false},
        {"clear outdoor path", 118, 124, 1, 0, false},
    }
    for _, edge in ipairs(edges) do
        local square = cell:getGridSquare(edge[2], edge[3], 0)
        if square then
            report(edge[1], square:testCollideAdjacent(player, edge[4], edge[5], 0), edge[6])
        else
            report(edge[1] .. " loaded", false, true)
        end
    end
    local roofCount, indoorCount = 0, 0
    for y = 120, 127 do
        for x = 120, 129 do
            local upper = cell:getGridSquare(x, y, 1)
            local ground = cell:getGridSquare(x, y, 0)
            if upper and upper:getFloor() then roofCount = roofCount + 1 end
            if ground and not ground:isOutside() then indoorCount = indoorCount + 1 end
        end
    end
    report("roof squares above room", roofCount, 80)
    report("room squares classified indoors", indoorCount, 80)
end

Events.OnGameStart.Add(runChecks)
