-- Optional read-only checks for the fictional cottage. Excluded from packages.
local function report(label, actual, expected)
    print("[Cottage QA] " .. (actual == expected and "PASS" or "FAIL") .. " " .. label
        .. " actual=" .. tostring(actual) .. " expected=" .. tostring(expected))
end

local function runChecks()
    local player, cell = getSpecificPlayer(0), getCell()
    if not player or not cell or player:getX() < 110 or player:getX() > 140
        or player:getY() < 110 or player:getY() > 140 then
        print("[Cottage QA] SKIP: player outside test area")
        return
    end
    for _, edge in ipairs({
        {"west wall", 120, 125, -1, 0, true},
        {"north wall", 121, 120, 0, -1, true},
        {"east wall", 125, 124, 1, 0, true},
        {"south wall", 121, 129, 0, 1, true},
        {"clear entry", 121, 123, 0, 1, false},
        {"clear outdoor path", 118, 123, 1, 0, false},
    }) do
        local square = cell:getGridSquare(edge[2], edge[3], 0)
        report(edge[1], square and square:testCollideAdjacent(player, edge[4], edge[5], 0), edge[6])
    end
    local roof, indoors, doors, windows, switches = 0, 0, 0, 0, 0
    for y = 120, 130 do
        for x = 120, 126 do
            local square = cell:getGridSquare(x, y, 0)
            if x < 126 and y < 130 then
                local upper = cell:getGridSquare(x, y, 1)
                if upper and upper:getFloor() then roof = roof + 1 end
                if square and not square:isOutside() then indoors = indoors + 1 end
            end
            if square then
                local objects = square:getObjects()
                for i = 0, objects:size() - 1 do
                    local obj = objects:get(i)
                    if instanceof(obj, "IsoDoor") then doors = doors + 1 end
                    if instanceof(obj, "IsoWindow") then windows = windows + 1 end
                    if instanceof(obj, "IsoLightSwitch") then switches = switches + 1 end
                end
            end
        end
    end
    report("ceiling coverage", roof, 60)
    report("indoor squares", indoors, 60)
    report("doors", doors, 3)
    report("windows", windows, 7)
    report("light switches", switches, 3)
end
Events.OnGameStart.Add(runChecks)
